import sys

n = int(input())
sangcard = list(map(int, sys.stdin.readline().split()))
m = int(input())
card = list(map(int, sys.stdin.readline().split()))

sangcard.sort()


for i in card:
	start = 0
	end = n-1
	mid = (start+end)//2

	while end-start >= 0:
		if sangcard[mid] == i :
			print("1",end=" ")
			break
		elif sangcard[mid] < i :
			start = mid +1
		else: 
			end = mid -1
		mid = (end+start)//2

	if sangcard[mid] != i : 
		print("0",end = " ")
