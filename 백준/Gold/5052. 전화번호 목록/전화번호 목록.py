import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
	n = int(input())
	li = []
	trg = 0
	for j in range(n):
		tmp = input().rstrip()
		li.append(tmp)
	li = sorted(li)

	for a,b in zip(li,li[1:]):
		if b.startswith(a):
			print("NO")
			trg = 1
			break

	if trg != 1:
		print("YES")