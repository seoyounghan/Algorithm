N, X = map(int, input().split())

li = list(map(int, input().split()))

for tmp in li:
	if tmp < X:
		print(tmp, end = " ")