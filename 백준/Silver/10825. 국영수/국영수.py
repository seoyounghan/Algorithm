import sys
input = sys.stdin.readline

N = int(input())

li = []

for i in range(0, N):
	name, a, b, c = input().split()
	li.append([name, int(a), int(b), int(c)])

li.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in li:
	print(i[0])