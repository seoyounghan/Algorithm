N = int(input())

li = [0]*(N+1) 

for i in range(2,N+1):

	li[i] = li[i-1] + 1

	if i % 3 == 0:
		li[i] = min(li[i],li[i//3]+1)
	if i % 2 == 0:
		li[i] = min(li[i],li[i//2]+1)
print(li[N])