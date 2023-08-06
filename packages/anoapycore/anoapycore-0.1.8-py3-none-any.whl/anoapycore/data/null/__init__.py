import numpy as __np
import pandas as __pd

def count (a_data) :
    return a_data.isnull().sum()
    
# check in any rows had more null than specific number 
# def greater_than (a_data,a_max_null) :
#    return a_data[a_data.isnull().sum(axis=1) > a_max_null]    
    
def percentage (a_data) :
    missing_info = __pd.DataFrame(__np.array(a_data.isnull().sum().sort_values(ascending=False).reset_index())\
                                ,columns=['Columns','Missing_Percentage']).query("Missing_Percentage > 0").set_index('Columns')
    return 100*missing_info/a_data.shape[0]    
    
def fill (a_data,a_columns,b_fill_with='NA') :
    a_data[a_columns] = a_data[a_columns].fillna(b_fill_with)    
    return a_data
