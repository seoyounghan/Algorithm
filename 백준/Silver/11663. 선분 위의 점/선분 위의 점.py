import sys
input = sys.stdin.readline

N, M  = map(int, input().split())

dotLi = list(map(int, input().split()))
dotLi.sort()

for i in range(M):
	A,B = sorted(list(map(int, input().split())))
	upperA = N-1
	lowerA = 0

	upperB = N-1
	lowerB = 0

	resA = -1
	resB = -1

	while 1:
		if upperA < lowerA:
			break

		mid = (upperA+lowerA)//2

		if dotLi[mid] == A:
			resA = mid
			break
		elif dotLi[mid] < A:
			lowerA = mid+1
		elif dotLi[mid] > A:
			upperA = mid-1

	if resA == -1:
		for j in range(mid-1, mid +2):
			if j>=0 and j<N and dotLi[j]>A:
				resA = j
				break


	while 1:
		if upperB < lowerB:
			break

		mid = (upperB+lowerB)//2

		if dotLi[mid] == B:
			resB = mid
			break
		elif dotLi[mid] < B:
			lowerB = mid+1
		elif dotLi[mid] > B:
			upperB = mid-1	

	if resB == -1:
		for j in range(mid+1, mid-2, -1):
			if j>=0 and j<N and dotLi[j]<B:
				resB = j
				break

	#print(resA, resB)	
	if resB-resA <0 or resB == -1 or resA == -1:
		print(0)
	else:
		print(resB-resA+1)
