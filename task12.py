def hist(string):
	new_dict = {}
	for key in string:
		if key not in new_dict:
			new_dict[key] = 1
		else:
			new_dict[key] += 1
	return new_dict


def inverse_dict(dictionary):
	new_dict_invert={}
	for key in dictionary:
		value = dictionary[key]
		if value not in new_dict_invert:
			new_dict_invert[value] = [key]
		else:
			new_dict_invert[value].append(key)
	return new_dict_invert



result = hist("hipopotamus")
print(result)

result2 = inverse_dict(result)
print(result2)
