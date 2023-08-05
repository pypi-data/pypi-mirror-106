import pytest
from wrapplotly.util import as_list
import numpy as np
import pandas as pd

class TestAsList:
    def test_1d_numpy(self):
        # 1D np.array
        expected = [0,1,2,3,4,5,6,7,8]
        result = as_list(np.arange(9))
        assert expected == result
    
    def test_2d_numpy(self):
        #2D np.array
        expected = [
            [0,1,2],
            [3,4,5],
            [6,7,8]
            ]
        result = as_list(np.arange(9).reshape(3,3))
        assert expected == result

    def test_3d_numpy(self):
        # 3D np.array
        expected = [
            [[1,2],
            [3,4]],
            [[5,6],
            [7,8]],
            [[9,10],
            [11,12]]
        ] 
        result = as_list(np.arange(1,13).reshape(3,2,2))
        assert expected == result

    def test_list(self):
        # list
        expected = [0,1,2,3,4,5,6,7,8]
        result = as_list([0,1,2,3,4,5,6,7,8])
        assert expected == result

    def test_str(self):
        # str
        expected = ['Vienna']
        result = as_list('Vienna')
        assert expected == result
    
    def test_pd_series(self):
        # pd.Series
        expected = [4,5,6]
        s = pd.Series([4, 5, 6])
        result = as_list(s)
        assert expected == result
    
    def test_pd_dataframe(self):    
        # pd.DataFrame
        df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
        error_msg = 'obj should be a string or list-like, not a pandas.DataFrame'
        with pytest.raises(TypeError, match = error_msg):
            as_list(df)
    
    def test_dict(self):
        # dict
        error_msg = 'obj should be a string or list-like, not a dict'
        with pytest.raises(TypeError, match = error_msg):
            as_list({'one':1, 'two': 2, 'three': 3})


# def test_as_list():
#     # 1D np.array
#     expected = [0,1,2,3,4,5,6,7,8]
#     result = as_list(np.arange(9))
#     assert expected == result

#     #2D np.array
#     expected = [
#         [0,1,2],
#         [3,4,5],
#         [6,7,8]
#         ]
#     result = as_list(np.arange(9).reshape(3,3))
#     assert expected == result
#     # 3D np.array
#     expected = [
#         [[1,2],
#         [3,4]],
#         [[5,6],
#         [7,8]],
#         [[9,10],
#         [11,12]]
#     ] 
#     result = as_list(np.arange(1,13).reshape(3,2,2))
#     assert expected == result
#     # list
#     expected = [0,1,2,3,4,5,6,7,8]
#     result = as_list([0,1,2,3,4,5,6,7,8])
#     assert expected == result
#     # str
#     expected = ['Vienna']
#     result = as_list('Vienna')
#     assert expected == result
#     # pd.Series
#     expected = [4,5,6]
#     s = pd.Series([4, 5, 6])
#     result = as_list(s)
#     assert expected == result
#     # pd.DataFrame
#     df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
#     error_msg = 'obj should be a string or list-like, not a pandas.DataFrame'
#     with pytest.raises(TypeError, match = error_msg):
#         as_list(df)
#     # dict
#     error_msg = 'obj should be a string or list-like, not a dict'
#     with pytest.raises(TypeError):
#         as_list({'one':1, 'two': 2, 'three': 3})
