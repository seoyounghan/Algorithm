import sys
import bisect

input = sys.stdin.readline

T = int(input())

n = int(input())
A = list(map(int,input().split()))

m = int(input())
B = list(map(int,input().split()))

sumA = []
sumB = []

for i in range(n):
	for j in range(i+1,n+1):
		sumA.append(sum(A[i:j]))

for i in range(m):
	for j in range(i+1,m+1):
		sumB.append(sum(B[i:j]))
sumA.sort()
sumB.sort()

ans = 0

for i in sumA:
	left = bisect.bisect_left(sumB,T-i)
	right = bisect.bisect_right(sumB,T-i)
	ans += right - left 
print(ans)