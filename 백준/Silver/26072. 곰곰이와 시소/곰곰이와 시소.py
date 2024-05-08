import sys
input = sys.stdin.readline

#받침점의 위치 X
# 무게 * 거리
# 거리 -> 왼쪽: X-chickens[i], 오른쪽: chickens[i]-X

N, L = map(int, input().split())

chickens = list(map(int, input().split()))
chickensWeights = list(map(int, input().split()))

top = N - 1
bottom = 0
ans = 0

while 1:
	if bottom > top:
		break

	mid = (bottom + top)//2
	Left = 0
	Right = 0

	for i in range(0, N):
		if i <= mid:
			Left += chickensWeights[i]*(chickens[mid] - chickens[i])
		else :
			Right += chickensWeights[i]*(chickens[i] - chickens[mid])

	if Left > Right:
		bottom = mid + 1
	elif Right < Left:
		top = mid - 1
	else :
		break
# print(Left, Right, mid)
div = 0
for i in range(0,N):

	ans += chickensWeights[i]*chickens[i]
	div += chickensWeights[i]
	
print('%f'%(ans/div))