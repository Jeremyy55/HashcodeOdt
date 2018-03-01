def deplacement(end,begin=[0,0]):
	#distance = delta x - delta y
	distance=abs(end[0]-begin[0])+abs(end[1]-begin[1])
	return int(distance)

