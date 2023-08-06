from . import column
from . import load
from . import null
from . import row
from . import save
from . import stat
from . import value

import pandas as __pd
from sklearn.preprocessing import MinMaxScaler as __minmax
from sklearn.preprocessing import StandardScaler as __standard

def copy (a_data) :
    """
    This function is aimed to copy one dataframe to another dataframe.
    This will prevent a dataframe to be affected by another dataframe.
    """
    return a_data.copy()

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

def normalize (a_data,a_column,b_method='MinMax') :
    """
    This function is aimed to normalize data.
    Use [] when passing parameter to a_column.
    Options for b_method = 'MinMax' (default),'Standard'
    Return directly to a_data[a_column]
    """
    if b_method == 'MinMax' :
        loc_scaler = __minmax()
        a_data[a_column] = loc_scaler.fit_transform(a_data[a_column])
    elif b_method == 'Standard' :
        loc_scaler = __standard()
        a_data[a_column] = loc_scaler.fit_transform(a_data[a_column])

