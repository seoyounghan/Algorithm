import sys
input = sys.stdin.readline

N = int(input())

inputLi = list(map(int, input().split()))
li = []

for i in range(N):
	li.append([i, inputLi[i]])

li.sort(key = lambda x: x[1])

prev = li[0][1] + 1
count = -1

for j in range(0, N):
	if prev != li[j][1] : 
		count += 1

	prev = li[j][1]
	li[j][1] = count

li.sort(key = lambda x: x[0])

for i in li:
	print(i[1], end = " ")
