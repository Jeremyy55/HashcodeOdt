from handleFile import *


def calculGauth(tab):
	for line in tab:
		if abs(line[2]-line[0])+abs(line[3]-line[1])<line[5]:
			print("ok")
		else:
			print("Dommage")
def main():
	damn = text2lines("data/a_example.in")
	print(len(damn))
	calculGauth(damn)

if __name__ == '__main__':
	main()
