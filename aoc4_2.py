i1 = []
i2 = []

inp = [4,75,74,31,76,79,27,19,69,46,98,59,83,23,90,52,87,6,11,92,80,51,43,5,94,17,15,67,25,30,48,47,62,71,85,58,60,1,72,99,3,35,42,10,96,49,37,36,8,44,70,40,45,39,0,63,2,78,68,53,50,77,20,55,38,86,54,93,26,88,12,91,95,34,9,14,33,66,41,13,28,57,29,73,56,22,89,21,64,61,32,65,97,84,18,82,81,7,16,24]

for i in range(100):
	for i in range(6):
		if i == 5:
			input()
			continue
		i1.append([int(k) for k in input().split()])
	i2.append(i1)
	i1 = []
print(i2)
f = False

ok = [0 for _ in range(100)]

for i in inp:
	#print(i)
	for ind1,i1 in enumerate(i2):
		for j in i1:
			if i in j:
				ind = j.index(i)
				j[ind] = -1
				if(sum(j)==-5 or i1[0][ind]==i1[1][ind]==i1[2][ind]==i1[3][ind]==i1[4][ind]==-1):
					#print("BINGO")
					su = 0
					for r in i1:
						for s in r:
							if s>-1:
								su+=s
					print(su*i)
					#print(i1)
					print("index "+str(ind1))
					ok[ind1] = 1
					print(ok)
					if sum(ok)==100:
						f = True
						
						print("ZAAAAAAAAAAAAAAAALA")
					break
		if f:
			break
	if f:
		break
		