import sys
input = sys.stdin.readline
n = int(input())

li = []

for _ in range(n):
	li.append(list(map(int,input().split())))

li.sort(key = lambda x :[x[1],x[0]])

endT = -1
count = 0

for i in li:
	if endT <= i[0]:
		endT = i[1]
		count += 1

print(count)