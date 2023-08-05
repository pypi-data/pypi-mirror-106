
#%%
import os
import abc
import pandas as pd
from datetime import datetime
from .config import data_path
from .tools import print_func_time,to_intdate

aindex_member = os.path.join(data_path,r'AIndexMembers')
aindex_membercitics = os.path.join(data_path,r'AIndexMembersCITICS')

ashare_description = os.path.join(data_path,r'AShareDescription')
ashare_st = os.path.join(data_path,r'AShareST')
ashare_suspension = os.path.join(data_path,r'AShareTradingSuspension')

ashare_idu_citics = os.path.join(data_path,r"AShareIndustriesClass_CITICS")
ashare_idu_sw = os.path.join(data_path,r'AShareIndustriesClass_SW')

class BaseStatusInfoProvider(abc.ABC):

    @abc.abstractmethod
    def get_status_data(self,instruments,fields,start_date,end_date):
        raise NotImplementedError

class LocalIndexStatusProvider(BaseStatusInfoProvider):

    def get_status_data(self,datapath,indexcode,start_date =None,end_date = None):
       
        df = pd.read_hdf(os.path.join(datapath,'all.h5'),"data")
        try:
            df = df.loc[indexcode]
            dfcp = df['outdate'].fillna(int(datetime.now().strftime("%Y%m%d")))
            if (start_date is not None) & (end_date is not None):
                start_date,end_date = to_intdate(start_date),to_intdate(end_date)
                df = df.loc[(df.indate <= end_date)&(dfcp >= start_date)]
            return df
        except KeyError:
            print('Index %s info not found'%indexcode)
            return pd.DataFrame()
    
    @print_func_time
    def index_member(self,indexcode,start_date =None,end_date = None):
        """ AIndexMembers """
        return self.get_status_data(aindex_member,indexcode,start_date,end_date)
    
    @print_func_time
    def index_member_citics(self,indexcode,start_date =None,end_date = None):
        """ AIndexMembersCITICS """
        return self.get_status_data(aindex_membercitics,indexcode,start_date ,end_date)
    
class LocalInstStatusProvider(BaseStatusInfoProvider):

    def get_status_data(self,datapath,stkcodes,fields = None):
        path = os.path.join(datapath,'all.h5')
        df = pd.read_hdf(path,'data')

        if stkcodes:
            if isinstance(stkcodes,str):
                stkcodes = [stkcodes,]
            df = df.loc[df.index.isin(stkcodes)]
            if fields:
                df = df[fields]
        df = df.dropna(how='all',axis=0)
        return df

    @print_func_time
    def list_instrument(self,univ,start_date,end_date):
        start_date,end_date = to_intdate(start_date),to_intdate(end_date)
        if univ == 'all':
            path = os.path.join(ashare_description,'all.h5')
            df = pd.read_hdf(path,'data')
            dfcp = df['delistdate'].fillna(int(datetime.now().strftime("%Y%m%d")))
            if (start_date is not None) & (end_date is not None):
                start_date,end_date = to_intdate(start_date),to_intdate(end_date)
                df = df.loc[(df.listdate <= end_date)&(dfcp >= start_date)]
            return df
        else:
            univ = stk_uiverse.get(univ)
            IdxSP = LocalIndexStatusProvider()
            return IdxSP.index_member(univ,start_date,end_date)

    @print_func_time
    def ashare_ipodate(self,stkcode,fields = None):
        """ AIndexMembers """
        return self.get_status_data(ashare_description,stkcode,fields)

    @print_func_time
    def ashare_st(self,stkcode,fields = None):
        """ AIndexMembers """
        return self.get_status_data(ashare_st,stkcode,fields)
            
    @print_func_time
    def ashare_suspension(self,stkcode,fields = None):
        """ AIndexMembers """
        return self.get_status_data(ashare_suspension,stkcode,fields)    

class LocalIndustryMemberProvider:

    @print_func_time
    def Industrycompo_citics(self,stockcode = None,level = None):
        path = os.path.join(ashare_idu_citics,'all.h5')
        df = pd.read_hdf(path,'data')
        if level:
            df = df[level]
        if stockcode:
            df = df.loc[stockcode]
        return df

    @print_func_time
    def Industrycompo_sw(self,stockcode = None,level = 'L1'):
        path = os.path.join(ashare_idu_sw,'all.h5')
        df = pd.read_hdf(path,'data')
        if level:
            df = df[level]
        if stockcode:
            df = df.loc[stockcode]
        return df

stk_uiverse = { "sz300":'000009.SH',  # 上证380
                "sz50" :'000016.SH',  # 上证50
                "zz500":'000852.SH',  # 中证1000
                "zz100":'000903.SH',  # 中证100
                "zz200":'000904.SH',  # 中证200
                "zz500":'000905.SH',  # 中证500
                "zz800":'000906.SH',  # 中证800
                "zxidx":'399005.SZ',  # 中小板指
                "cyidx":'399006.SZ',  # 创业板指
                "sz300":'399007.SZ',  # 深圳300
                "zx300":'399008.SZ',  # 中小300
                "hs300":'399300.SZ',  # 沪深300
                "zzall":'399985.SZ'}  # 中证全指