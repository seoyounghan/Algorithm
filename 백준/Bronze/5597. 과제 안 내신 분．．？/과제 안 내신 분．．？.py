li = [0]*31

li[0] = 1

for _ in range(28):
	tmp = int(input())

	li[tmp] = 1

for i in range(31):
	if li[i] == 0:
		print(i)