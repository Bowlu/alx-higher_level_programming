#!/usr/bin/python3
def uniq_add(my_list=[]):
	add = 0
	uniq_int = set(my_list)
	for x in uniq_int:
		add += x

	return add
