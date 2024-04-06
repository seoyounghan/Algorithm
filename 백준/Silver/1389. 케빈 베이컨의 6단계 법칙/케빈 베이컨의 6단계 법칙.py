import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
friendList = []
bestFriend = [[0]*(N+1) for _ in range(N+1)]
ans = float("inf")
realAns = 0

def bfs(num):
	global ans
	global realAns
	tmp = 0
	q= deque([(num, 0)])
	visited = [False]*(N+1)
	visited[num] = True
	while len(q)>0:
		friendNum, friendCount = q.popleft()
		tmp += friendCount
		for i in range(1, N+1):
			if (bestFriend[friendNum][i] == 1) and (visited[i] == False):
				q.append((i, friendCount+1))
				visited[i] = True

	if ans> tmp:
		ans = tmp
		realAns = num


for i in range(M):
	a,b = map(int, input().split())
	bestFriend[a][b] = 1
	bestFriend[b][a] = 1

for i in range(1, N+1):
	bfs(i)

print(realAns)