def cummulative_sum(lst):
	summ=0
	holder=[]
	for i in lst:
		summ += i
		holder.append(summ)
	print (holder)


cummulative_sum([1,2,3,4,5,6])
