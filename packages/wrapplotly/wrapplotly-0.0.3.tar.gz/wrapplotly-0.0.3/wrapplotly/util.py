from copy import deepcopy
import numpy as np
import pandas as pd

def as_list(obj):
    '''
    Converts all strings and list-likes to a list.
    Raises errors is given a dict or pandas.DataFrame
    '''
    def recur(arr):
        if len(arr.shape) == 1:
            return list(arr)
        else:
            res = [recur(arr[i]) for i in range(arr.shape[0])]
            return res  

    obj = deepcopy(obj)
    if isinstance(obj, list):
        return obj
    elif isinstance(obj, str):
        return [obj]
    elif isinstance(obj, np.ndarray):
        return recur(obj)
    elif isinstance(obj, pd.DataFrame):
        error_msg = 'obj should be a string or list-like, not a pandas.DataFrame'
        raise TypeError(error_msg)
    elif isinstance(obj, dict):
        error_msg = 'obj should be a string or list-like, not a dict'
        raise TypeError(error_msg)
    else:
        return list(obj)



