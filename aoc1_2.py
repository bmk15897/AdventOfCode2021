
inp1 = [int(input()),int(input()),int(input())]

m = 0
for i in range(1997):
	print(inp1)
	m1 = sum(inp1)
	inp1 = inp1[1:]
	inp2 = inp1
	inp2.append(int(input()))
	print(inp2)
	m2 = sum(inp2)
	if m2>m1:
		m+=1
	inp1 = inp2	
print(m)