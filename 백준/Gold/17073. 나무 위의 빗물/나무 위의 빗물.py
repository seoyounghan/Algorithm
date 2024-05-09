import sys
input = sys.stdin.readline

N, W = map(int, input().split())
li = {}
count = 0

for i in range(N-1):
	a, b = map(int, input().split())

	for j in (a,b):
		if j in li:
			li[j] += 1
		else:
			li[j] = 1


for k,v in li.items():
	if k != 1 and v == 1:
		count+=1

print(W/count)
