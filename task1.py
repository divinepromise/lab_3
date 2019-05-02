nested = [[34, 5], [78,34,56], [-9, 97, -123]]

def nested_sum(integer_list):
	total=0
	for element in integer_list:
		total+= sum(element)
	print(total)



nested_sum(nested)
