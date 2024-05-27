import sys
input = sys.stdin.readline

N = int(input())

li = set([])

for _ in range(N):
	a, b = input().rstrip().split()

	if b == "enter":
		li.add(a)
	else :
		li.remove(a)

lis = list(li)
lis.sort(reverse = True)

for i in lis:
	print(i)

