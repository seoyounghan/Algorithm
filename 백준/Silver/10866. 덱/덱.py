import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
li = deque([])

for _ in range(N):
	tmp = list(input().split())
	if tmp[0] == "push_front":
		li.appendleft(tmp[1])
	elif tmp[0] == "push_back":
		li.append(tmp[1])
	elif tmp[0] == "pop_front":
		if li:
			print(li.popleft())
		else:
			print(-1)
	elif tmp[0] == "pop_back":
		if li:
			print(li.pop())
		else:
			print(-1)
	elif tmp[0] == "size":
		print(len(li))
	elif tmp[0] == "empty":
		if li:
			print(0)
		else:
			print(1)
	elif tmp[0] == "front":
		if li:
			print(li[0])
		else:
			print(-1)
	elif tmp[0] == "back":
		if li:
			print(li[-1])
		else:
			print(-1)