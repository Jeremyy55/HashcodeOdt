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

def text2lines(filename):
	file=open(filename,"r")
	lines=file.readlines()
	print("lines")
	print(lines)
	output=[]
	for line in lines:
		print("line")
		print(line)
		print("line.split")
		output.append(line.split())
	return output

def extract1line(tab):
	firstLine=tab[0]
	tab.remove(firstLine)
	return firstLine,tab

	
