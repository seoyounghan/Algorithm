N = list(input())
N.sort(reverse = True)

for i in N[:-1]:
	print(i, end = '')
print(N[-1])