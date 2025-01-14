import sys

input = sys.stdin.readline

K, N = map(int, input().split())

li = []
for _ in range(K):
	li.append(int(input()))

def getCount(a):
	sum = 0
	for i in range(K):
		sum += (li[i]//a)
	return sum

left = 1
right = max(li)
ans = 0

while left<=right :
	mid = (left+right)//2
	if getCount(mid)>=N:
		ans = mid
		left = mid + 1
	else :
		right = mid - 1
print(ans)