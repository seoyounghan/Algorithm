from collections import deque

N,M = map(int,input().split())

li = []
q = deque()
board = []

for i in range(N):
	li.append(list(input()))
	board.append(list(map(int,li[i])))

q.append([0,0])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
	a,b = q.popleft()

	for i in range(4):
		nx = a + dx[i]
		ny = b + dy[i]

		if (0 <= nx < N) and (0 <= ny < M) and (board[nx][ny] == 1):
			q.append([nx,ny])
			board[nx][ny] = board[a][b] + 1

print(board[N-1][M-1])

		

