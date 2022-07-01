import sys

li = []

n = int(input())

for i in range(n):
	li.append(int(sys.stdin.readline()))

li = list(set(li))
li.sort()

for i in range(len(li)):
	print(li[i])