
import os
import platform

if(platform.system()=='Windows'):
    print('Windows系统')
    data_path = os.path.join("Z:\\","qtDOperation","Jtjjdata","data")
elif platform.system()=='Linux':
    print('Linux系统')
    data_path = os.path.join("/mnt/z/","qtDOperation","Jtjjdata","data")
    

provider_config = {
    "CTDP": "CTradeDayInfoProvider",
    "STDP": "STradeDayInfoProvider",
    "BP": "LocalPorvider",
    "IdxSP": "LocalIndexStatusProvider",
    "InstSP": "LocalInstStatusProvider",
    "InduSP": "LocalIndustryMemberProvider",
    "FRP": "LoacalFincReportsProvider"
}