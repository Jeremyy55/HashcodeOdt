
from handleFile import *

def init(tab):
	car=[]
	for i in range(int(tab)) :
		car.append([0,0,0])
	return car
def feasable(tab):
	for line in tab:
		if abs(int(line[2])-int(line[0]))+abs(int(line[3])-int(line[1]))<int(line[5]):
			return True
		else:
			return False

def deplacement(tab):
	if feasable(tab):
		print("ok")
def main():
	damn = text2lines("data/a_example.in")
	print(len(damn))

	[R, C, F, N, B, T], already = extract1line(damn)
	print('test test')
	print(R)
	print(C)
	print(already)
	car = init(F)
	print(car)
	#deplacement(damn)

if __name__ == '__main__':
	main()
