i1 = []
i2 = []

a = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
	i1.append(input())
	i2.append(i1[-1])

temp1 = []
temp2 = []

g = i1
e = i2
o = []
c = []
for i in range(12):
	g1 = []
	g2 = []
	e1 = []
	e2 = []
	if len(g)==1:
		o = g
	else:
		for j in g:
			if j[i] == '1':
				g1.append(j)
			else:
				g2.append(j)
		if len(g1)>=len(g2):
			g = g1
			o.append('1')
		else:
			g = g2
			o.append('0')
		
	if len(e)==1:
		c = e
	else:
		for j in e:
			if j[i] == '0':
				e1.append(j)
			else:
				e2.append(j)	
		
		if len(e1)==len(e2):
			e = e1
			c.append('0')
		elif len(e1)>len(e2):
			e = e2
			c.append('1')
		else:
			e = e1
			c.append('0')
	print(o,c)
print(int("".join(o),2) * int("".join(c),2))