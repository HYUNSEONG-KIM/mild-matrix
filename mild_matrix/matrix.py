from collections import Iterable
from typing import Union, Tuple


class Matrix:
    def __init__(self, data_list, dim:Union[int, Tuple[int, int]]):
        self._data = data_list
        self.dim = tuple(dim) if isinstance(dim, Iterable) else [dim]
        self.rank= len(self.dim)


        self.square  = False
        self.sparse  = False
        self.hermit  = False
        self.unitary = False
    
    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __rmul__(self, other):
        pass
    
    @property
    def diagonal(self):
        if self.square:
            l = []
            for i in range(self.dim[0]):
                l.append(self._data[i][i])
        return l
    def tp(self):
        #transpose
        pass
    def tr(self):
        #trace
        pass
    def dagger(self):
        pass

    def det(self):
        pass
    def sub_block_matrix(self):
        pass
    
    def concatenate(self, other, axis):
        # concatentae [M, other] or [[M], [other]]
        pass

    def eigen(self):
        pass

    def reshape(self, shape):
        pass
    def flip(self, axis):
        pass


