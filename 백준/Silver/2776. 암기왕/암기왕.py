import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	N = int(input())
	note1 = list(map(int, input().split()))

	M = int(input())
	note2 = list(map(int, input().split()))

	note1.sort()
	for i in note2:
		left = bisect_left(note1, i)
		right = bisect_right(note1, i)
		if right - left > 0:
			print("1")
		else:
			print("0")