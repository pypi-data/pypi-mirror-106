# data.column.value

from . import null

import numpy as __np
import multipledispatch as __dispatch

@__dispatch.dispatch(object,str,str,int)
def replace (a_data,a_column,a_old,a_new) :
    a_data[a_column].replace(a_old,a_new,inplace=True)

@__dispatch.dispatch(object,str,list,list)
def replace (a_data,a_column,a_old,a_new) :
    i = 0
    for x in a_old :
        i = i + 1
        a_data[a_column].replace(x,a_new[i-1],inplace=True)

def unique (a_data,a_column) :
    return list(__np.unique(a_data[a_column]))
