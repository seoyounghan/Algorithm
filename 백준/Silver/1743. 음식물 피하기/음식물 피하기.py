from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())

li = [[0]*(M+1) for _ in range(N+1)]
q = deque()

ans = 1
ans1 = 0

for _ in range(K):
	x,y = map(int, input().split())

	li[x][y] = 1

for i in range(1,N+1):
	for j in range(1,M+1):
		if li[i][j] == 1:
			if len(q) == 0:
				q.append([i,j])
				li[i][j] = 0
				ans1 = max(ans, ans1)
				ans = 1
			while len(q) > 0:
				x,y = q.popleft()
				if li[x-1][y] == 1:
					q.append([x-1,y])
					li[x-1][y] = 0
					ans += 1
				if li[x][y-1] == 1:
					q.append([x,y-1])
					li[x][y-1] = 0
					ans += 1
				if (x+1 <= N) and (li[x+1][y] == 1):
					q.append([x+1,y])
					li[x+1][y] = 0
					ans +=1
				if (y+1 <= M) and (li[x][y+1] == 1):
					q.append([x,y+1])
					li[x][y+1] = 0
					ans += 1
			ans1 = max(ans, ans1)
print(ans1)

