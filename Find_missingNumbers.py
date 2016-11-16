'''
	You are presented with two arrays, all containing 
	positive integers. One of the arrays will have one 
	extra number
'''
def find_missing(a, b):
	if a == [] and b == [] or a == b:
	 	return 0
	for item in a:
		if item not in b:
			return item 
	for item in b:
		if item not in a:
			return item

print find_missing([1, 5, 11], [1, 5, 3, 11])
