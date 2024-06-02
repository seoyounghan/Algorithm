import sys

input = sys.stdin.readline

N = int(input())

li = set(["ChongChong"])



for _ in range(N):
	A, B = input().rstrip().split()

	if A in li or B in li:
		li.add(B)
		li.add(A)

print(len(li))