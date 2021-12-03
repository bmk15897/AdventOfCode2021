i1 = []
a = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
	i1.append(input())
	if i1[-1][0] == '1':
		a[0] +=1
	if i1[-1][1] == '1':
		a[1] +=1
	if i1[-1][2] == '1':
		a[2] +=1
	if i1[-1][3] == '1':
		a[3] +=1
	if i1[-1][4] == '1':
		a[4] +=1
	if i1[-1][5] == '1':
		a[5] +=1
	if i1[-1][6] == '1':
		a[6] +=1
	if i1[-1][7] == '1':
		a[7] +=1
	if i1[-1][8] == '1':
		a[8] +=1
	if i1[-1][9] == '1':
		a[9] +=1
	if i1[-1][10] == '1':
		a[10] +=1
	if i1[-1][11] == '1':
		a[11] +=1
		
g = []
e = []

for i in a:
	if i>500:
		g.append('1')
		e.append('0')
	else:
		e.append('1')
		g.append('0')
print("".join(g))
print("".join(e))
print(int("".join(g),2) * int("".join(e),2))