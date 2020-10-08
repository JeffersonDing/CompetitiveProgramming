rules = []
data = []
count = 0
for i in range(0,3):
	rules.extend(input().split())
data.extend(input().split())

def r1(a):
	if(a.find(rules[0])!=-1):
		a.replace(rules[0],rules[1])
		count+=1

def r2(b):
	if(a.find(rules[2])!=-1):
		data[1].replace(rules[2],rules[3])
		count+=1
def r3(c):
	if(a.find(rules[6])!=-1):
		data[1].replace(rules[4],rules[5])
		count+=1


			
