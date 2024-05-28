import sys
input = sys.stdin.readline

di = {}

N, M = map(int, input().split())

for _ in range(N):
	A, B = input().rstrip().split()

	di[A] = B

for _ in range(M):
	A = input().rstrip()
	print(di[A])