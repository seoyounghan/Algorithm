N = int(input())

li = list(map(int, input().split()))

s = sum(li)

res = 0

for i in li:
	s = s - i
	res += s*i

print(res)

