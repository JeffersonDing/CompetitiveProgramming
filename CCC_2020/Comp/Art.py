times=int(input())
coordinates=[]
xcoordinates=[]
ycoordinates=[]
bottomleftx=0
bottomlefty=0
toprightx=1000
toprighty=1000
for x in range(0,times):
    coordinates.append(input().split(','))
for y in coordinates:
    xcoordinates.append(int(y[0]))
    ycoordinates.append(int(y[1]))


print(str(sorted(xcoordinates)[0]-1)+','+str(sorted(ycoordinates)[0]-1))
print(str(sorted(xcoordinates)[len(xcoordinates)-1]+1)+','+str(sorted(ycoordinates)[len(ycoordinates)-1]+1))
