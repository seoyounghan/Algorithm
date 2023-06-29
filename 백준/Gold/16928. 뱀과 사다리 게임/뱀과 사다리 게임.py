from collections import deque

N,M = map(int,input().split())
ladder = []
board = [-1]*101

q = deque()

for _ in range(N+M):
	x,y = map(int,input().split())
	ladder.append([x,y])


count = 0

q.append(1)
board[1] = 0


while 1:
    gom = q.popleft()
    for i in range(1,7):
        if board[gom+i] != -1:
            continue
        else : 
            board[gom+i] = board[gom]+1
        token = 1
        for j,k in ladder:
            if (gom+i) == j:
                if board[k] == -1:
                	q.append(k)
                	board[k] = board[gom]+1
                token = 0
        if token == 1:
        	q.append(gom+i)
        	if gom + i == 100:
        		count = board[gom] + 1
        		
        		print(count)
        		
        		exit()
        	



