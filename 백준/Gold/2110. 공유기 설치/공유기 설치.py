import sys
input = sys.stdin.readline

N,C = map(int, input().split())

li = []

for _ in range(N):
	li.append(int(input()))

li.sort()

def getDistance(a):
	count = 0
	tmp = li[0]
	for i in range(N):
		if li[i]>=tmp:
			count += 1
			tmp = li[i] + a
	return count

left = 0
right = int(1e9)
ans = 0
while left<=right:
	mid = (left+right)//2
	if getDistance(mid) >= C :
		left = mid + 1
		ans = max(mid,ans)
	else :
		right = mid - 1

print(ans) 