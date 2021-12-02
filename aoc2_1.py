h = 0
d = 0

for i in range(1000):
	i1 = input()
	if i1[0]=='f':
		h += int(i1[8:])
	elif i1[0]=='u':
		d -= int(i1[3:])
	elif i1[0]=='d':
		d += int(i1[5:])
	
print(d*h)