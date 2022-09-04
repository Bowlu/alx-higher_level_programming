#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_List = []
    for x in matrix:
	new_List.append(list(map(lambda x: x**2, x)))
return (new_List)
