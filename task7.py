def is_sorted(lst):
	holder=[]
	for value in lst:
		holder.append(value)
	if holder == sorted(holder):
		return True
	else:
		return False


result1 = is_sorted([1,2,2,3])
result2 = is_sorted(['b','a'])
print(result1)
print(result2)
