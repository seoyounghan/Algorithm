n = int(input())

max3count = n//3
max5count = n//5

for i in range(max5count,-1,-1) :
	count = 0
	for j in range(max3count,-1,-1):
		count = 5*i + 3*j
		if count == n:
			print(i+j)
			break
	if count == n:
		break

if count != n:
	print("-1")