from handleFile import *

def main():
	damn = text2lines("data/a_example.in")
	print(len(damn))
	#calculGauth(damn)
	[R,C,F,N,B,T],already=extract1line(damn)
	print('test test')
	print(R)
	print(C)
	print(already)

if __name__ == '__main__':
	main()
