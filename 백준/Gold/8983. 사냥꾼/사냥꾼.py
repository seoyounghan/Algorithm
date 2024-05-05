import sys
input = sys.stdin.readline

M,N,L = map(int, input().split())
saDae = list(map(int, input().split()))
saDae.sort()

animals = []

def lengthAni(x,a,b):
	return abs(x-a)+b

for i in range(N):
	animals.append(list(map(int, input().split())))

res = 0

for animal in animals:
	minI = 0
	maxI = M-1

	while 1:
		if minI > maxI:
			break
		mid = (minI+maxI)//2

		if lengthAni(saDae[mid],animal[0],animal[1]) <= L:
			res += 1
			break
		elif animal[0] == saDae[mid]:
			break
		elif animal[0] > saDae[mid]:
			minI = mid + 1
		else:
			maxI = mid - 1
print(res)


