from handleFile import *


def calculGauth(tab):
	for line in tab:
		if abs(int(line[2])-int(line[0]))+abs(int(line[3])-int(line[1]))<int(line[5]):
			print("ok")
		else:
			print("Dommage")
def main():
	damn = text2lines("data/a_example.in")
	print(len(damn))
	calculGauth(damn)

if __name__ == '__main__':
	main()
