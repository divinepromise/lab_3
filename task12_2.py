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
		value = dictionary.setdefault(key, None)

		new_dict_invert[value].append[key]
	return new_dict_invert
'''		value = dictionary[key]
		if value not in new_dict_invert:
			new_dict_invert[value] = [key]
		else:
			new_dict_invert[value].append(key)
	return new_dict_invert

dict = {'Name': 'Zara', 'Age': 7}
print "Value : %s" %  dict.setdefault('Age', None)
print "Value : %s" %  dict.setdefault('Sex', None)
'''

result = hist("hipopotamus")
print(result)

result2 = inverse_dict(result)
print(result2)
