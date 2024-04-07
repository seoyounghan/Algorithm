import sys
from collections import deque
input = sys.stdin.readline

computerNum = int(input().rstrip())
M = int(input().rstrip())
ans = 0

networkList = [[0]*(computerNum+1) for _ in range(computerNum+1)]

for _ in range(M):
	a, b = map(int, input().split())

	networkList[a][b] = 1
	networkList[b][a] = 1

visited = [False for _ in range(computerNum+1)]
q = deque([1])
visited[1] = True

while q:
	qNum = q.popleft()
	for i in range(1, computerNum+1):
		if (visited[i] == False) and (networkList[qNum][i] == 1):
			q.append(i)
			visited[i] = True
			ans += 1

print(ans)