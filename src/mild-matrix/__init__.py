# Copyright (c) 2022, Hyunseong Kim <qwqwhsnote@gm.gist.ac.kr>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# 1, 2 dimension matrix operation based on default list type

import collections
from math import sin, cos, sqrt
from random import random

# Default operation - vector
# basis routines
def __vec_oper1(vec, oper=lambda i, vi: vi, *args):
    length= len(vec)
    result = []*length
    for i in range(0, length):
        result = oper(i, vec[i], args)
    return result
def __vec_oper2(vec1, vec2, oper=lambda i, vi1, vi2: vi1 + vi2, *args):
    length= len(vec1)
    if length != len(vec2):
        raise ValueError("Two vectors do not have same length.")
    result = []*length
    for i in range(0, length):
        result = oper(i, vec1[i], vec2[i], args)
    return result

def __add(i, v1 ,v2, args):
        return v1+v2
def __sub(i, v1, v2, args):
        return v1-v2
def __mul(i, v1, v2, args):
        return v1*v2
def __add_c(i, v, args):
    return v+args[0]
def __sub_c(i, v, args):
    return v-args[0]
def __mul_c(i, v, args):
    return v*args[0]

# Default operation - vector - interfaces
def vec_add(vec1, vec2):
    return __vec_oper2(vec1, vec2, __add)
def vec_sub(vec1, vec2):
    return __vec_oper2(vec1, vec2, __sub)
def vec_mul(vec1, vec2):
    return __vec_oper2(vec1, vec2, __mul)
def vec_add_c(vec1, const):
    return __vec_oper1(vec1, __add_c, const)
def vec_sub_c(vec1, const):
    return __vec_oper1(vec1, __sub_c, const)
def vec_mul_c(vec1, const):
    return __vec_oper1(vec1, __mul_c, const)

def vec_dot(vec1, vec2):
    return sum(vec_mul(vec1, vec2))

def vec_norm_euclid(vec):
    return sqrt(vec_dot(vec, vec))

# Default operation - matrix
def __matrix_oper1(matrix, oper, *args):
    pass

def matrix_add(matrix1, matrix2):
    row = len(matrix1)
    column = len(matrix1[0])

    result = [[]*column]*row
    for i in range(0, row):
        for j in range(0, column):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def matrix_substract(matrix1, matrix2):
    row = len(matrix1)
    column = len(matrix1[0])

    result = [[]*column]*row
    for i in range(0, row):
        for j in range(0, column):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result

def matrix_multiply(matrix1, matrix2):
    row = len(matrix1)
    column = len(matrix1[0])

    result = [[]*column]*row
    for i in range(0, row):
        for j in range(0, column):
            result[i][j] = matrix1[i][j] * matrix2[i][j]
    return result

# Default operation - matrix-vec, matrix-matrix
def matrix2vec(matrix, vec):
    size = len(vec)
    result =[]
    for row in matrix:
        element = 0
        for i in range(0, size):
            element += row[i] * vec[i]
        result.append(element)
    return result
def matrix2matrix(matrix1, matrix2):

    size_row1 = len(matrix1)
    size_column1 = len(matrix1[0])
    size_row2 = len(matrix2)
    size_column2 = len(matrix2[0])

    if size_row1 != size_column2 or size_column1 != size_row2:
        raise ValueError("Matrix dimensions are not matched each other.")

    matrix2_t = transpose(matrix2)

    result = []

    for j, column in enumerate(matrix2_t):
        result[j] = matrix2vec(matrix1, column)
    
    return transpose(result)


# Special matrixes
def __matrix(dim1, dim2, gen= lambda i, j : i+j, *args):
    pass
def ones_matrix(dim1, dim2):
    return [[1]*dim2]*dim1
def zeros_matrix(dim1, dim2):
    return [[0]*dim2]*dim1
def rand_matrix(dim1:int, dim2:int, type="int", range=(0,10)):
    # If we get 10x10 matrix, manually mapping  requires 100 time call but, 
    # what if we call 20=(10 x 10) random values and mutiplying them?
    # It is not enough to get randomness? 

    result = [[]*dim2]*dim1
    for i in range(0, dim1):
        for j in range(0, dim2):
            result[i][j] = random()
    return result

# Special matrixes - Rotation
def rotate_2dim(vec, angle):
    rotate_matrix = rotation_matrix_2dim(angle)
    return matrix2vec(rotate_matrix, vec)
def rotate_3dim(vec, angle, axis):
    rotate_matrix = rotation_matrix_3dim(angle, axis)
    return matrix2vec(rotate_matrix, vec)
def rotation_matrix_2dim(angle):
    return [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]
def rotation_matrix_3dim_x(angle):
    return [[1, 0         , 0          ],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle) ]]
def rotation_matrix_3dim_y(angle):
    return [[cos(angle) , 0, 0         ],
            [0          , 1, sin(angle)],
            [-sin(angle), 0, cos(angle)]]
def rotation_matrix_3dim_z(angle):
    return [[cos(angle) , -sin(angle), 0],
            [sin(angle) , cos(angle) , 0],
            [0          , 0          , 1]]
def rotation_matrix_3dim(angle, axis =0):
    if axis == 0:
        return rotation_matrix_3dim_x(angle)
    elif axis == 1:
        return rotation_matrix_3dim_y(angle)
    elif axis == 2:
        return rotation_matrix_3dim_z(angle)
def rotation_matrix_3dim_general(angle_x, angle_y=None, angle_z=None):
    if angle_y == None and len(angle_x) ==3:
        angle_y = angle_x[1]
        angle_z = angle_x[2]
        angle_x = angle_x[0]
    rm_x = rotation_matrix_3dim_x(angle_x)
    rm_y = rotation_matrix_3dim_y(angle_y)
    rm_z = rotation_matrix_3dim_z(angle_z)

    return matrix2matrix(rm_z, matrix2matrix(rm_y, rm_x))


def identity_matrix(dim):
    identity = zeros_matrix(dim,dim)
    for i in range(0, dim):
        identity[i][i] =1
    return identity
def exchange_matrix(dim):
    identity = zeros_matrix(dim,dim)
    for i in range(0, dim):
        identity[i][dim-1-i] =1
def permutation_matrix(permute:list):
    dim = len(permute)
    permutation_m = zeros_matrix(dim,dim)
    for i in range(0, dim):
        permutation_m[i][permute[i]-1] = 1
    return permutation_m
#def vandermonde_matrix(xlist, n): <- Is there an efficient algorithm for calculating repeated powers ?
#    pass


# Matrix utils -general


# Matrix utils - square
def get_diagonal(matrix, i:int = 0):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Not a square matrix.")
    size = len(matrix)
    if abs(i) >= size:
        raise ValueError("Order exceeds size.")
    length = (size - abs(i))
    result = [] * (length)
    for row_index in range(0, length):
        j = row_index + i
        result[row_index] = matrix[row_index][j]
    return result
def get_trace(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Not a square matrix.")
    result = 0
    for i in range(0, len(matrix)):
        result += matrix[i][i]
    return result
def get_determinant(matrix):
    pass



# Utils

def split_list(list1d: list, n: int, mode="l") -> list:
    if not isinstance(list1d, collections.Iterable):
        raise TypeError("The given object is not an iterable object.")
    if mode != "l" and mode != "n":
        raise ValueError("The 'mode' parameter must be 'l' or 'n', current = {mode}")
    num = n
    length_list = len(list1d)
    if mode == "n":
        if length_list % num != 0:
            raise ValueError(
                "The length of the given list and the sublist length must have a divider relationship."
            )
        num = int(length_list / num)
        mode = "l"
    if mode == "l":
        if num <= 1:
            return list1d
        if len(list1d) % num != 0:
            raise ValueError(
                f"The length of sublist, {num}, must be a divider of original list, {len(list1d)}. "
            )
        rlist = []
        for i in range(0, int(length_list / num)):
            ni = num * i
            rlist.append([list1d[ni : ni + num]][0])
    return rlist

def transpose(list2d: list) -> list:
    row_length = len(list2d)
    column_length = len(list2d[0])
    t = list()
    for i in range(0, column_length):
        t.append([])
    for i in range(0, column_length):
        for j in range(0, row_length):
            t[i].append(list2d[j][i])
    return t

def filp(matrix: list) -> list:
    size = len(matrix)
    f = list()
    for i in range(0, size):
        f.append(matrix[size - i - 1])
    return f

def concatenate(matrix: list[list]) -> list:
    length = len(matrix)
    rlist = list()
    for i in range(0, length):
        for element in matrix[i]:
            rlist.append(element)
    return rlist

def reshape(list1d: list, shape) -> list[list]:
    size1d = len(list1d)
    if size1d != shape[0] * shape[1]:
        raise ValueError("The list length and shape are not matched each other.")
    return split_list(list1d, shape[0], mode="n")


