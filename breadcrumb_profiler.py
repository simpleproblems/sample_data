
Pin-Ju Tien <pinju.tien@gmail.com>
Tue, Jul 24, 2018, 10:36 PM
to me

import psutil
import pandas as pd

class breadcrumber(object):
    
    def __init__(self):
        self.summary = []
        self.report_cols = ["tag", "time", "mem_total", "mem_available", "mem_used", "mem_free"]
    def drop(self, tag):        
        self.summary += [[tag, 
                          psutil.cpu_times().user,
                          psutil.virtual_memory().total,
                          psutil.virtual_memory().available,
                          psutil.virtual_memory().used,
                          psutil.virtual_memory().free
                         ]]
        
    def get_summary_df(self):
        return pd.DataFrame(self.summary, columns = self.report_cols)
        
        

profiling_obj = breadcrumber()

import time
for i in range(10):
    drop_name = "tag_{x}".format(x = i)
    profiling_obj.drop(drop_name)
    time.sleep(4)
    
    
