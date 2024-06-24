import sys
input = sys.stdin.readline

N = int(input())
res = 0 

for i in range(N):
	tmp = input()
	prev = ""
	li = []
	flag = 0
	for j in tmp:
		if prev != j:
			if j in li:
				flag = 1
			li.append(j)
		prev = j

	if flag == 0:
		res += 1


print(res)