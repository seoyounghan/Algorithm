import copy
import sys
input = sys.stdin.readline
N = int(input())

li = []

for i in range(N):
	a = list(input())
	li.append(a)

li2 = copy.deepcopy(li)
stack1 = []
stack2 = []
count1 = 0
count2 = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find1(x,y,rgb):
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if 0<=nx<N and 0<=ny<N and li[nx][ny] != 0 and rgb == li[nx][ny]:
			stack1.append([nx,ny])

def find2(x,y,rgb):
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if 0<=nx<N and 0<=ny<N and li2[nx][ny] != 0 :
			if (rgb == "R" or rgb == "G") and (li2[nx][ny] == "R" or li2[nx][ny] == "G"): 
				stack2.append([nx,ny])
			elif rgb == li2[nx][ny] :
				stack2.append([nx,ny])

for i in range(N):
	for j in range(N):
		if li[i][j] != 0:
			rgb = li[i][j]
			stack1.append([i,j])
			li[i][j] = 0	
			while stack1:
				x,y=stack1.pop()
				find1(x,y,rgb)
				li[x][y] = 0
			count1 += 1

for i in range(N):
	for j in range(N):
		if li2[i][j] != 0:
			stack2.append([i,j])
			rgb = li2[i][j]
			li2[i][j] = 0
			while stack2:
				x2,y2 = stack2.pop()
				find2(x2,y2,rgb)
				li2[x2][y2] = 0
			count2 += 1

print(count1, count2)



