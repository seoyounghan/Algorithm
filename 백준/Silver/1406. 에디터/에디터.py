import sys

input = sys.stdin.readline

Lli = list(input().rstrip())
Rli = []

M = int(input())

for _ in range(M):
	a = input().split()

	if a[0] == "L" :
		if len(Lli) >= 1:
			Rli.append(Lli.pop())
	elif a[0] == "D":
		if len(Rli) >=1:
			Lli.append(Rli.pop())
	elif a[0] == "B":
		if len(Lli) >=1:
			Lli.pop()
	elif a[0] == "P":
		Lli.append(a[1])

Lli.extend(reversed(Rli))

print(''.join(Lli))

