def split(word):
	return [char for char in word]


Data = split(input())
a = 1
b = 2
c = 3
d = 4
firstrow = [a,b]
secondrow = [c,d]

def H():
	global firstrow
	global secondrow
	temp = firstrow
	firstrow = secondrow
	secondrow = temp
def V():
	global firstrow
	global secondrow
	temp1 = firstrow[0]
	firstrow[0] = firstrow[1]
	firstrow[1] = temp1

	temp2 = secondrow[0]
	secondrow[0] = secondrow[1]
	secondrow[1] = temp2
for x in Data:
	if(x == 'H'):
		H()
	elif(x == 'V'):
		V()
for p in firstrow:
	print(p,end = '')
print('\n')
for q in secondrow:
	
	print(q,end = '')