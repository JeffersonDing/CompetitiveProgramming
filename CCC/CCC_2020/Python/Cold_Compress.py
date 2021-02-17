a = input()
b = 1
fin = []
final = []
def AddtoBuf(a,b):
	fin.append(str(a))
	fin.append(b)

for i in range(0,int(a)):
	buffer = input()
	buf = list(buffer)
	buf.append(' ')
	for q in range(0,len(buf)-1):
		if(buf[q]==buf[q+1]):
			b+=1
		elif(buf[q]!=buf[q+1]):
			AddtoBuf(b,buf[q])
			b=1
	final.append(''.join(fin))
	fin = []

for line in final:
	print(line)