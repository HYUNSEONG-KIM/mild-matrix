# mild-matrix

Mild matrix routines written in pure python routines.

## Background
[Numpy](https://numpy.org/) is a wonderful library to provide various N-dimension array routines with hight speed and stability.
However, what about for python projects requiring matrix routines but not a huge project? 
Numpy is too heavy for those project, especially, Linux version needs double space than Windows version.
mild-matrix package is a simple matrix routine implmentations based on list type of python.

## Specification

Does not provide additional class all the routines are just manipulate list elements.
If you want to require class implmented module, you can use [matrix](https://github.com/AnonymouX47/matrix) by [AnonymouX47](https://github.com/AnonymouX47?tab=repositories) 

## Features

### Matrix

1, 2 dimension matrix routines

vector : 1dim list.
Matrix : 2dim list, row-major order.

* Basic vector, matrix add, sub, mul, div routines.
* Constant add, sub, mul, div for vector and matrix. 
* Matrix->vec, Matrix->Matrix products.
* Special matrixes: Random, Random_integer, Identity, Permutation, Exchange, Rotation, ... .
* Matrix properties: diagonal, determinant, trace, transpose,
* Utils: flip, split_list, concatenate, reshape vector -> Matrix or Matrix -> vector.
