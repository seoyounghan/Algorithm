n = int(input())
count = 0
max5Count = n//5
max2Count = n//2

for i in range(max5Count,-1,-1):
	tmp5 = i*5
	tmp = 0
	for j in range(max2Count+1,-1,-1):
		tmp2 = j*2
		tmp = tmp5+tmp2
		if tmp == n:
			count = i+j
			print(i+j)
			break
	if tmp == n:
			break
if count == 0:
	print("-1")
