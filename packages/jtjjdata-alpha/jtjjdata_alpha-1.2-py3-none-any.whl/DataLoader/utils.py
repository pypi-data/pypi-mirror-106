
from threading import Thread
from .tools import print_func_time,bisect_left,bisect_right
from .calendarpd import Tdcal

import pandas as pd
import numpy as np
import numba as nb
import h5py

calendar,calendar_index = Tdcal._get_calendar(freq = 'Tdays')

class Mythread(Thread):

    def __init__(self,target,args,name = '',**kwargs):
        Thread.__init__(self)
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self.name = name

    @property
    def result(self):
        return getattr(self,'_result',None)
    
    def run(self):
        """Method representing the thread's activity."""
        try:
            if self._target:
                self._result = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

class BatchH5Reader:

    @staticmethod
    def read_h5_m(path,indexloc,fields,cindex_level):
        try:
            # df = pd.read_hdf(path,'data').reindex(indexloc,level = cindex_level).loc[:,fields]
            # df = pd.read_pickle(path).reindex(indexloc,level = cindex_level).loc[:,fields]
            df = pd.read_hdf(path,'data')[fields]
            df = df.loc[df.index.get_level_values(level = cindex_level).isin(indexloc)]
        except FileNotFoundError:
            df = pd.DataFrame(columns=fields)
        return df
    
    @staticmethod
    def read_h5_s(path,indexloc,fields):
        df = pd.read_hdf(path,'data').reindex(indexloc)[fields]
        return df
    
    @print_func_time
    def batch_reader(self,pathlist,instruments,fields,reader = 'read_h5_m',cindex_level = 0):
        Threads = []
        for path in pathlist:
            Threads.append(Mythread(target = getattr(BatchH5Reader,reader),args = (path,instruments,fields,cindex_level)))
        for thread in Threads:
            thread.start()
        for thread in Threads:
            thread.join()
        dfs = [thread.result for thread in Threads if not thread.result.empty]
        return dfs

def read_mergeh5(path,ori_instruments,fields,start_index,end_index,tidx = 'trade_dt'):
    instruments = [''.join(inst.split('.')[::-1]) for inst in ori_instruments]
    with h5py.File(path,'r') as h5:
        instlist = h5['instlist'][:].astype(str)            # inst code list
        instloc = h5['instloc'][:]     
        rsilist = h5['rsilist'][:]
        reilist = h5['reilist'][:]  
        dset = h5['data']  
        cidx = dset.shape[0]  
        
        infoloc = np.where(np.in1d(instlist,instruments))
        availbles = np.array(ori_instruments)[np.where(np.in1d(instruments,instlist))[0]]
        mask,amount = gen_idxs(cidx,infoloc,instloc,rsilist,reilist,start_index,end_index)

        if fields:
            if isinstance(fields,str):
                fields = [fields]
            if isinstance(tidx,list):
                data = dset[(mask,*tidx,*fields)]
            else:
                data = dset[(mask,tidx,*fields)]
        else:
            data = dset[mask]

        data = pd.DataFrame(data).dropna(axis = 0,how = 'all')
        data['code'] = np.repeat(availbles,amount)
        return data

def gen_idxs(cidx,infoloc,instloc,rsilist,reilist,start_index,end_index):
    mask = np.zeros(cidx,dtype = bool)
    amount = []
    for i in infoloc[0]:
        instsiloc = instloc[i]
        tsi,tei = max(start_index - rsilist[i],0), max(min(end_index - rsilist[i], reilist[i] - rsilist[i]),0)
        h5si,h5ei = tsi + instsiloc,tei + instsiloc
        amount.append(h5ei - h5si + 1)
        mask[h5si:h5ei + 1] = True
    return mask,amount

@nb.jit(nopython = True,cache=True)
def match_amt(value,idx,ref_stt_idx,ref_end_idx):
    value = np.append([np.nan],value)
    fidx = np.append([ref_stt_idx],idx)
    bidx = np.roll(fidx,-1)
    bidx[-1] = ref_end_idx + 1
    amt = bidx - fidx
    return value,amt

@print_func_time
def to_ndns_reports(df,value_label,start_date,end_date,key1 = 'report_period',key2 = 'ann_date'):
    df['si'] = df[key2].apply(lambda x:bisect_left(calendar,x))
    dfs = {}
    ref_stt_idx = bisect_left(calendar,int(start_date))
    ref_end_idx = bisect_right(calendar,int(end_date)) - 1
    index = Tdcal.calendar(start_date,end_date)
    for inst,df_i in df.groupby(df['code']):
        df_i = df_i.sort_values([key2,key1]).drop_duplicates(key2,keep='last')
        value,amt = match_amt(df_i[value_label].values,df_i.si.values,ref_stt_idx,ref_end_idx)
        dfs[inst] = np.repeat(value,amt)
        assert dfs[inst].shape[0] == 3492
    return pd.DataFrame(dfs,index = index)