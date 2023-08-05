
#%%
import os
import abc
import pandas as pd
from .config import data_path
from .tools import print_func_time,to_intdate,get_yearlist
from .utils import BatchH5Reader,read_mergeh5
from .calendarpd import Tdcal

ashare_eod_price = os.path.join(data_path,r'AShareEODPrices')
ashare_blocktrade = os.path.join(data_path,r'AShareBlockTrade')
ashare_derivative_indicator = os.path.join(data_path,r'AShareEODDerivativeIndicator')
ashare_dividend_record = os.path.join(data_path,r'AShareEXRightDividendRecord')
ashare_l2_indicator = os.path.join(data_path,r'AShareL2Indicators')
ashare_margin_trade = os.path.join(data_path,r'AShareMarginTrade')
ashare_money_flow = os.path.join(data_path,r'AShareMoneyFlow')
ashare_tech_indicator = os.path.join(data_path,r'AShareTechIndicators')
ashareyield = os.path.join(data_path,r'AShareYield')

aswsindexeod = os.path.join(data_path,r'ASWSIndexEOD')
aindex_eod_price = os.path.join(data_path,r'AIndexEODPrices')
aindex_idueodcitics = os.path.join(data_path,r'AIndexIndustriesEODCITICS')
#%%
class BaseDailyTSInfoProvider(abc.ABC):

    @abc.abstractmethod
    def get_daily_data(self,instruments,fields,start_date,end_date):
        raise NotImplementedError


class CTradeDayInfoProvider(BaseDailyTSInfoProvider):
    """ Intensive time sereis data with trade day as index """

    tidx = 'trade_dt'
    def get_daily_data(self,datapath,instruments,fields,start_date,end_date):
        path = os.path.join(datapath,'merged.h5')
        start_index,end_index = Tdcal.locate_index(start_date,end_date,freq = 'Tdays')
        return read_mergeh5(path,instruments,fields,start_index,end_index,self.tidx)

    @print_func_time
    def get_daily_share_data(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(ashare_eod_price,instruments,fields,start_date,end_date)

    @print_func_time
    def get_daily_share_deridi(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(ashare_derivative_indicator,instruments,fields,start_date,end_date)

    @print_func_time
    def get_daily_share_l2idi(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(ashare_l2_indicator,instruments,fields,start_date,end_date)

    @print_func_time
    def get_daily_moneyflow(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(ashare_money_flow,instruments,fields,start_date,end_date)

    @print_func_time
    def get_daily_techindi(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(ashare_tech_indicator,instruments,fields,start_date,end_date)

    @print_func_time
    def get_daily_yield(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(ashareyield,instruments,fields,start_date,end_date)

    @print_func_time
    def get_daily_index_data(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(aindex_eod_price,instruments,fields,start_date,end_date)

    @print_func_time
    def get_daily_index_industries(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(aindex_idueodcitics,instruments,fields,start_date,end_date)

    @print_func_time
    def get_daily_aswsindexeod(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(aswsindexeod,instruments,fields,start_date,end_date)

class STradeDayInfoProvider(BaseDailyTSInfoProvider,BatchH5Reader):
    """ sparse time sereis data with trade day as index """

    @print_func_time
    def get_daily_data(self,datapath,instruments,fields,start_date,end_date):
        pathlist = [os.path.join(datapath,fn + '.h5') for fn in get_yearlist(start_date,end_date)]
        df_list = self.batch_reader(pathlist,instruments,fields,reader = 'read_h5_m',cindex_level = 0)

        sd,ed = to_intdate(start_date),to_intdate(end_date)
        df_list[0] = df_list[0].loc[df_list[0].index.get_level_values(level = 'trade_dt') > sd]
        df_list[-1] = df_list[-1].loc[df_list[-1].index.get_level_values(level = 'trade_dt') < ed]

        multidxdf = pd.concat(df_list,axis=0)
        return multidxdf
    
    @print_func_time
    def get_daily_share_divdrec(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(ashare_dividend_record,instruments,fields,start_date,end_date)
    
    @print_func_time
    def get_daily_blocktrade(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(ashare_blocktrade,instruments,fields,start_date,end_date)

    @print_func_time
    def get_daily_margintrade(self,instruments,fields,start_date,end_date):
        return self.get_daily_data(ashare_margin_trade,instruments,fields,start_date,end_date)


# %%
