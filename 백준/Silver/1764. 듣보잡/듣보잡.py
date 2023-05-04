import sys

input = sys.stdin.readline

N,M = map(int,input().split())

allName = set()
nName = set()
mName = set()

for _ in range(N):
	tmp = input()
	allName.add(tmp)
	nName.add(tmp)

for _ in range(M):
	tmp = input()
	allName.add(tmp)
	mName.add(tmp)

ans = []

for name in allName :
	if name in nName and name in mName:
		ans.append(name)

ans.sort()

print(len(ans))

for an in ans:
	print(an.strip())