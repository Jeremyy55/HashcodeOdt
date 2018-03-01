from handleFile import *
from forCar import *
from ride import *
def main():
	damn = text2lines("data/a_example.in")
	print(len(damn))

	[R, C, F, N, B, T], already = extract1line(damn)
	print('test test')
	print(R)
	print(C)
	print(already)
	cars = init(F)
	print(cars)
	steps=0
	while(steps < int(T)) :
		for car in cars:
			for ride in already:
				if feasable(car, ride):
					goForRide(cars,already,car,ride)
					steps+=1

if __name__ == '__main__':
	main()
