import pytz,pandas as pd, numpy as np,datetime as dt,pickle, os, glob
from dorianUtils.configFilesD import ConfigDashTagUnitTimestamp

class ConfigFilesBuilding(ConfigDashTagUnitTimestamp):
    # ==========================================================================
    #                       INIT FUNCTIONS
    # ==========================================================================

    def __init__(self,folderPkl,pklMeteo=None,folderFig=None,folderExport=None,encode='utf-8'):
        self.appDir         = os.path.dirname(os.path.realpath(__file__))
        self.filePLC = glob.glob(self.appDir +'/confFiles/' + '*PLC*')[0]
        super().__init__(folderPkl,self.filePLC,folderFig=folderFig,folderExport=folderExport)
        # self.typeGraphs = pd.read_csv('confFiles/typeGraph.csv',index_col=0)
        self.usefulTags     = pd.read_csv(self.appDir+'/confFiles/predefinedCategories.csv',index_col=0)
        self.rsMinDefault   = 15
        self.listCompteurs  = pd.read_csv(self.appDir + '/confFiles/compteurs.csv')
        self.listVars       = pd.read_csv(self.appDir + '/confFiles/variables.csv')
        self.dfPLCMonitoring = self._buildDescriptionDFplcMonitoring(encode)
        self.dfMeteoPLC     = self._loadPLCMeteo()
        self.dfPLC          = self._mergeMeteoMonitoringPLC()
        self.listUnits          = list(self.dfPLC.UNITE.unique())
        self.listCalculatedVars = None
        self.pklMeteo       = pklMeteo
        self.folderPkl       = folderPkl
        self.listFilesMeteo     = self.utils.get_listFilesPklV2(self.pklMeteo)

    def exportToxcel(self,df):
        df.index = [t.astimezone(pytz.timezone('Etc/GMT-2')).replace(tzinfo=None) for t in df.index]
        df.to_excel(dt.date.today().strftime('%Y-%m-%d')+'.xlsx')

    def getListVarsFromPLC(self):
        def getListCompteursFromPLC(self,regExpTagCompteur='[a-zA-Z][0-9]+-\w+'):
            return list(np.unique([re.findall(regExpTagCompteur,k)[0] for k in self.dfPLC.TAG]))
        listVars = self.getTagsTU(getListCompteursFromPLC()[0])
        listVars = [re.split('(h-)| ',k)[2] for k in listVars]
        return listVars

    def _loadPLCMeteo(self):
        dfPLC       = pd.read_csv(self.appDir + '/confFiles/configurationMeteo.csv')
        dfPLC.TAG = dfPLC.TAG.apply(lambda x: x.replace('SIS','SIS-02'))
        return dfPLC

    def _buildDescriptionDFplcMonitoring(self,encode):
        dfi = pd.read_csv(self.filePLC,encoding=encode)
        print('dfi.index:',dfi.index)
        for k in dfi.index:
            # print('dfi.iloc[' + str(k)+',0] : ',dfi.iloc[k,0])
            for l in self.listCompteurs.index:
                if self.listCompteurs.iloc[l,0] in dfi.iloc[k,0] :
                    compteurName = self.listCompteurs.iloc[l,1]
            for l in self.listVars.index:
                if self.listVars.iloc[l,0] in dfi.iloc[k,0] :
                    varName = self.listVars.iloc[l,1]
            desName = varName + ' ' + compteurName
            dfi.iloc[k,2] = desName
        return dfi

    def _mergeMeteoMonitoringPLC(self):
        tagToday    = self._getListMeteoTags()
        dfMeteoPLC  = self.dfMeteoPLC[self.dfMeteoPLC.TAG.isin(tagToday)]#keep only measured data not predictions
        return pd.concat([self.dfPLCMonitoring,dfMeteoPLC])

    def _getListMeteoTags(self):
        return list(self.dfMeteoPLC[self.dfMeteoPLC.TAG.str.contains('-[A-Z]{2}-01-')].TAG)

    # ==========================================================================
    #                       COMPUTATIONS FUNCTIONS
    # ==========================================================================
    def computePowerEnveloppe(self,timeRange,tagPat = 'VIRTUAL.+[0-9]-JTW',rs=None):
        if not rs : rs=str(self.rsMinDefault*60)+'s'
        df = self.loadDFTimeRange(timeRange)
        df = self.getDFTagsTU(df,tagPat,'W')
        df = self.pivotDF(df,resampleRate='5s',applyMethod='nanmean')

        L123min = df.min(axis=1)
        L123max = df.max(axis=1)
        L123moy = df.mean(axis=1)
        L123sum = df.sum(axis=1)
        df = pd.concat([df,L123min,L123max,L123moy,L123sum],axis=1)
        df = df.resample(rs).apply(np.nanmean)
        dfmin = L123min.resample(rs).apply(np.nanmin)
        dfmax = L123max.resample(rs).apply(np.nanmax)
        df = pd.concat([df,dfmin,dfmax],axis=1)

        df.columns=['L1_mean','L2_mean','L3_mean','PminL123_mean','PmaxL123_mean',
                    'PmoyL123_mean','PsumL123_mean','PminL123_min','PmaxL123_max']
        return df

    def loadFileMeteo(self,filename):
        if '*' in filename :
            filenames=self.utils.get_listFilesPklV2(self.pklMeteo,filename)
            if len(filenames)>0 : filename=filenames[0]
            else :return pd.DataFrame()
        tagToday = self._getListMeteoTags()
        df       = pickle.load(open(filename, "rb" ))
        df.tag  = df.tag.apply(lambda x:x.replace('@',''))#problem with tag remove @
        df.tag   = df.tag.apply(lambda x:x.replace('_','-'))#
        df      = df[df.tag.isin(tagToday)]#keep only measured data not predictions
        df.timestampUTC=pd.to_datetime(df.timestampUTC,utc=True)# convert datetime to utc
        return df

    def loadFileMonitoring(self,filename):
        if '*' in filename :
            filenames=self.utils.get_listFilesPklV2(self.folderPkl,filename)
            if len(filenames)>0 : filename=filenames[0]
            else : return pd.DataFrame()
        df = pickle.load(open(filename, "rb" ))
        return df

    def loadDF_TimeRange_Tags(self,timeRange,tags,rs='auto',applyMethod='mean',tzSel='Europe/Paris'):
        listDates,delta = self.utils.datesBetween2Dates(timeRange,offset=1)
        if rs=='auto':rs = '{:.0f}'.format(max(1,delta.total_seconds()/3600)) + 's'
        dfs = []
        for d in listDates:
            print(d)
            dfMonitoring  = self.loadFileMonitoring('*'+d+'*')
            dfMeteo       = self.loadFileMeteo('*'+d+'*')
            if 'tag' in dfMonitoring.columns : dfMonitoring = self.getDFfromTagList(dfMonitoring,tags)
            if 'tag' in dfMeteo.columns : dfMeteo = self.getDFfromTagList(dfMeteo,tags)
            df = pd.concat([dfMonitoring,dfMeteo],axis=0,ignore_index=True)
            if len(df.columns)>0:
                df = self.utils.pivotDataFrame(df,colPivot='tag',colValue='value',colTimestamp='timestampUTC',resampleRate=rs,applyMethod=applyMethod)
                dfs.append(df)
        #     # remvove the part of the dataframe that expands over the next date
        #     # remove doublons at the end when data are pivoted is an alternative as well
        #     if not '00-00' in filename:
        #         t0      = df.timestamp.iloc[0]
        #         tmax    = t0+dt.timedelta(days=1)-dt.timedelta(hours=t0.hour,minutes=t0.minute,seconds=t0.second+1)
        #         df      = df[df.timestamp<tmax]
        #     dfs.append(df)
        if not dfs : print('there are no files to load')
        else :
            df=pd.concat(dfs,axis=0)
            print(dfs)
            df.index=df.index.tz_convert(tzSel)# convert utc to tzSel timezone
            return self.getDFTimeRange(df,timeRange,'index')

    # def buildCalculatedVars(self,) :
