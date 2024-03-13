import sys
import copy
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
li = []
gradLi = []
ans = 0
blank = 0


def check(A,B,C,li):
	q = deque([])
	for i in range(N):
		for j in range(M):
			if li[i][j] == 2:
				q.append((i,j))
	li[A[0]][A[1]] = 1
	li[B[0]][B[1]] = 1
	li[C[0]][C[1]] = 1
	checking = blank

	while q:
		x, y = q.popleft()
		for i in range(4):
			X = dx[i] + x
			Y = dy[i] + y
			if 0 <= X < N and 0 <= Y < M :
				if li[X][Y] == 0 :
					li[X][Y] = 2
					q.append((X,Y))
					checking -= 1

	return checking



for _ in range(N):
	tmp = list(map(int,input().split()))
	li.append(tmp)

for i in range(N):
	for j in range(M):
		if li[i][j] == 0:
			gradLi.append((i,j))
			blank += 1

blank = blank - 3

for i in range(len(gradLi)):
	A = gradLi[i]
	if  i + 2 >= len(gradLi):
		continue
	for j in range(i+1,len(gradLi)):
		B = gradLi[j]
		for h in range(i+2,len(gradLi)):
			C = gradLi[h]
			copyli = copy.deepcopy(li)
			maxans = check(gradLi[i], gradLi[j], gradLi[h], copyli)
			ans = max(maxans,ans)

print(ans)






