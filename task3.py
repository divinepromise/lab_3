from functools import reduce

def sum_of_square():
	return reduce(lambda x,y:x+y, map(lambda x:x**2, range(0,11,2)))

result = sum_of_square()
print(result)
