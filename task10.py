def hist(string):
	new_dict={}
	for key in string:
		if key not in new_dict:
			new_dict[key] = 1
		else:
			new_dict[key] += 1
	return new_dict


def concise_hist(string):
	result = hist(string)
	new_result = result.get("a",-1)
	print(new_result)



concise_hist("hippoaaaaaaaaaaaaapokjnhgdhhhhde")
