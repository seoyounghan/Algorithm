from collections import deque
import sys

input = sys.stdin.readline

q = deque([])

N = int(input())

for _ in range(N):
	a = input().split()
	if a[0] == "push":
		q.append(int(a[1]))
	elif a[0] == "pop":
		if len(q) != 0:
			tmp = q.pop()
			print(tmp)
		else :
			print("-1")
	elif a[0] == "size" :
		print(len(q))
	elif a[0] == "empty":
		if len(q) == 0:
			print("1")
		else :
			print("0")
	elif a[0] == "top":
		if len(q) == 0:
			print("-1")
		else :
			print(q[len(q)-1])
	#print(q)

