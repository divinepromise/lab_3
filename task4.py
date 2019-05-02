def multiples_of_five():
	holder=[]

	lst_numbers = [1,5,10,13,25,89,90,120]

	for value in lst_numbers:
		if value%5==0:
			holder.append(value)
	return holder


result = multiples_of_five()
print(result)
