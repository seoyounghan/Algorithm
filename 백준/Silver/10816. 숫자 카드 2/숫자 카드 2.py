import sys

input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
dic = {}
for i in nlist:
	if i in dic:
		dic[i] += 1
	else:
		dic[i] = 1

m = int(input())
mlist = list(map(int, input().split()))

for i in mlist:
	if i in dic:
		print(dic[i], end = " ")
	else:
		print(0, end = " ")