from . import load
from . import column
from . import row
from . import stat

def dimension (a_dataframe) :
    print (str(row.count(a_dataframe)) + ' rows x ' + str(column.count(a_dataframe)) + ' columns')
       
def sample (a_data,a_row=5) :
    return a_data.head(a_row)

