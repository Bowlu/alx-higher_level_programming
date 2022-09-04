#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_List = []
    for x in matrix:
	new_List.append([y ** 2 for y in x])
    return new_List
