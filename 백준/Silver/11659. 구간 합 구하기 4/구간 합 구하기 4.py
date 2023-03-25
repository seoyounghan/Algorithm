import sys
input = sys.stdin.readline

N, M = map(int,input().split())

li = list(map(int,input().split()))
liSum = [0]*(N+1)

for i in range(1,N+1):
	liSum[i] = liSum[i-1] + li[i-1]



for k in range(M):
	i,j = map(int,input().split())

	print(liSum[j] - liSum[i-1])
