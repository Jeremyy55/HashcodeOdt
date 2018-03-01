def text2words(filename):
	file=open(filename,"r")
	lines=file.readlines()
	print("lines")
	print(lines)
	words=[]
	for line in lines:
		print("line")
		print(line)
		for word in line.split():
			print("word")
			print(word)
			words.append(word)
		print(words)
	return words
