def word_play3():
	word = open("words.txt")

	word_list=[]
	for line in word:
		line=line.strip()
		word_list.append(line)

	#word_list_dict = {i: word_list[i] for i in range(0,len(word_list))} 
	
	word_list_dict = {i:0 for i in word_list}

	print (word_list_dict)


word_play3()
