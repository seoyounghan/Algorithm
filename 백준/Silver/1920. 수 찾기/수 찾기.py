N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for i in B :
	high = N - 1
	low = 0
	while 1 :
		mid = (high + low)//2
		if high<low :
			print("0")
			break

		if i > A[mid] :
			low = mid +1 
		elif i < A[mid] :
			high = mid - 1
		else :
			print("1")
			break
