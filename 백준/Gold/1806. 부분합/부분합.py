import sys
input = sys.stdin.readline

N,S = map(int, input().split())
li = list(map(int,input().split()))

start = 0
end = 0
ans = 100001
tmp = li[0]

while end < len(li):
	if S<=tmp:
		ans = min(ans, end-start+1)
		start += 1 
		tmp = tmp - li[start - 1]
	else:
		end += 1
		if end < len(li):
			tmp = tmp + li[end]

if ans == 100001:
	print(0)
else :
	print(ans)