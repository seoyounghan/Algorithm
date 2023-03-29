import sys
input = sys.stdin.readline

# R = 0, G = 1, B = 2

N = int(input())

li=[]
count = [[0]*3 for _ in range(N)]

for i in range(N):
	li.append(list(map(int, input().split())))

count[0][0] = li[0][0]
count[0][1] = li[0][1]
count[0][2] = li[0][2]

for i in range(1,N):
	for j in range(3):
		if j == 0:
			count[i][j] = min(count[i-1][1],count[i-1][2]) + li[i][0]
		elif j == 1:
			count[i][j] = min(count[i-1][0],count[i-1][2]) + li[i][1]
		elif j == 2:
			count[i][j] = min(count[i-1][0],count[i-1][1]) + li[i][2]

print(min(count[N-1][0],count[N-1][1],count[N-1][2]))