from functools import reduce


def addition(x,y):
	return x+y

def using_reduce():
	return reduce(addition, range(100,501))



result = using_reduce()
print(result)

