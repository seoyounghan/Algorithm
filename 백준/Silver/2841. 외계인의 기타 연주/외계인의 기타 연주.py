import sys
input = sys.stdin.readline

N, P = map(int, input().split())

li = [[], [], [], [], [], []]

ans = 0

for i in range(N):
	A, B = map(int, input().split())

	if li[A-1]:
		while li[A-1]:
			if li[A-1][-1] > B:
				ans+=1
				li[A-1].pop()
			else:
				break
		if li[A-1] and li[A-1][-1] == B:
			continue
		ans += 1
		li[A-1].append(B)
	else:
		ans += 1
		li[A-1].append(B)

print(ans)