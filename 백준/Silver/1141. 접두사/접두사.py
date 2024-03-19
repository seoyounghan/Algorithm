import sys
input = sys.stdin.readline

N = int(input())
li = []
prev = "2"
for i in range(N):
	li.append(input().rstrip())

ans = len(li)
li.sort()

for i in li:
	if i.startswith(prev):
		ans -= 1

	prev = i

print(ans)