N = int(input())

li = [["*"]*N for _ in range(N)]

def erease(a,b,c,d):
	count = (1+c-a)//3
	for i in range(a+count,c-count+1):
		for j in range(b+count,d-count+1):
			li[i][j] = " "
			#print(i,j)

num = 3
while num <= N:
	for i in range (0,N-num+1,num):
		for j in range (0,N-num+1,num):
			erease(i,j,i+num-1,j+num-1)
	num = num*3

for i in range(N):
	for j in range(N):
		print(li[i][j], end = '')

	print()