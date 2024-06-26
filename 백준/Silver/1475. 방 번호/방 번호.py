N = input()

res = 0

for i in range(0, 9):
	if i != 6 and i != 9:
		tmp = N.count(str(i))
	else:
		tmp = (N.count("6") + N.count("9"))//2 + (N.count("6") + N.count("9"))%2

	res = max(res, tmp)

print(res)