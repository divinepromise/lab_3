
def histogram(string):
	new_dict={}
	for key in string:
		if key not in new_dict:
			new_dict[key] = 1
		else:
			new_dict[key] += 1
	return new_dict

result = histogram("pineapple")

print(sorted(result))

hold = []
for key in result:
	print (key,result[key])


for key in sorted(result):
	print (key,result[key])
