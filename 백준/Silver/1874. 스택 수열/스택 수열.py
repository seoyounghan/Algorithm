import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
tok = 1

for i in range(n):
	num = int(input())
	while tok <= num:
		stack.append(tok)
		ans.append("+")
		tok += 1
	if stack[-1] == num:
		stack.pop()
		ans.append("-")
	else: 
		print("NO")
		exit()

for i in ans:
	print(i)