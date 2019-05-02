def capitalize_all(nested_string):

	holder=[]
	for letter in nested_string:
		if letter.isupper()==True:
			holder.append(letter)
		else:
			letter=letter.upper()
			holder.append(letter)
	return holder


result = capitalize_all(["s","Angle","circle","g","S"])
print(result)
