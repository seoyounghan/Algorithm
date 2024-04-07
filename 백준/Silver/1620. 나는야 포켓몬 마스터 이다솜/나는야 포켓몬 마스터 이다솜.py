import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poketmonlist = ["first"]

for _ in range(N):
	poketmonlist.append(input().rstrip())

for _ in range(M):
	tmp = input().rstrip()

	if tmp.isnumeric():
		tmp = int(tmp)
		print(poketmonlist[tmp])
	else:
		tmpIndex = poketmonlist.index(tmp)
		print(tmpIndex)