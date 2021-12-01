
inp1 = int(input())
m=0
for i in range(1999):
	inp2 = int(input())
	if inp2>inp1:
		m+=1
	inp1 = inp2	
print(m)