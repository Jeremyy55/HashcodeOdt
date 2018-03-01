
from handleFile import *
from forCar import *

def init(tab):
	car=[]
	for i in range(int(tab)) :
		car.append([0,0,0])
	return car
def feasable(car, ride):
	move1=int( deplacement([int(car[0]),int(car[1])],[int(ride[0]),int(ride[1])]))
	move2=int( deplacement([int(ride[0]),int(ride[1])],[int(ride[2]),int(ride[3])]))
	if(car[2]+move1+move2)<int(ride[5]):
			#+<

		return True
	else:
		return False

#def deplacement(tab):
#	if feasable(tab):
#		print("ok")
def main():
	damn = text2lines("data/a_example.in")
	[R, C, F, N, B, T], already = extract1line(damn)
	car = init(F)
	print(feasable(car[0],already[0]))

if __name__ == '__main__':
	main()
