import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
S = int(input())

p = 0
count = 0

for i in range(N):
	if not S:
		break

	maxNum = max(li[i:i+S+1])
	maxIndex = li.index(maxNum)

	while maxIndex != i and S:
		li[maxIndex], li[maxIndex - 1] = li[maxIndex-1], li[maxIndex]
		maxIndex -= 1
		S -= 1

for i in li :
	print(i, end = " ")