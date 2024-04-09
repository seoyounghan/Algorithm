import sys
input = sys.stdin.readline

N = int(input())

li = []


for _ in range(N):
	li.append(input())

for i in range(N):
	count = 0
	for j in range(len(li[i]) - 1): 
		if li[i][j] == "(":
			count += 1
		else :
			count -= 1

		if count < 0:
			count = -51

	if count == 0:
		print("YES")
	else:
		print("NO")