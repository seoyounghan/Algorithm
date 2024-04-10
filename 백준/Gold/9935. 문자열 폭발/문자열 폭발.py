import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
bomb = list(input().rstrip())
bombLen = len(bomb)
ans = []

for i in str1:
	ans.append(i)
	if ans[len(ans)-bombLen:] == bomb:
		for _ in range(bombLen):
			ans.pop()

if len(ans) == 0:
	print("FRULA")
else :
	print(*ans, sep = "")