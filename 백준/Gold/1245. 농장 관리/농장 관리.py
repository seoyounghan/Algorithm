import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
Li = []
Ans = 0
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]
checkID = []


def searchLi(x, y, checkID):
	q = deque([(x,y)])
	Visited[x][y] = False
	check = [(x,y)]
	while q :
		X,Y = q.popleft()
		for i in range(8):
			nx,ny = X + dx[i], Y + dy[i]
			if nx<0 or ny<0 or nx >=N or ny >=M :
				continue
			if Visited[nx][ny] == False:
				continue
			if Li[X][Y]<Li[nx][ny]:
				return 0
			if Li[X][Y]==Li[nx][ny]:
				Visited[nx][ny] = False
				q.append((nx,ny))
				check.append((nx,ny)) 
		checkID += check
	return 1

for _ in range(N) :
	tmp = list(map(int,input().split()))
	Li.append(tmp)

for i in range(N):
	for j in range(M):
		if (i, j) not in checkID :
			Visited = [[True]*M for _ in range(N)]
			Ans += searchLi(i,j, checkID)


print(Ans)
