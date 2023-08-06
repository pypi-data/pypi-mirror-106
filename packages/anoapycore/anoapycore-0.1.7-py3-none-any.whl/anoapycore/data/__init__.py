from . import column
from . import load
from . import null
from . import row
from . import save
from . import stat
from . import value

import pandas as __pd

def dimension (a_dataframe) :
    print (str(row.count(a_dataframe)) + ' rows x ' + str(column.count(a_dataframe)) + ' columns')
       
def sample (a_data,a_row=5) :
    return a_data.head(a_row)

def info (a_data) :
    return a_data.info()
    
def merge (a_data_1,a_data_2) :
    """
    Merge 2 dataframes by index
    """
    loc_new_df = __pd.merge(a_data_1,a_data_2,left_index=True,right_index=True)
    return loc_new_df

