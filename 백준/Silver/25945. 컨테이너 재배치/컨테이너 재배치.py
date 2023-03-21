n = int(input())
a = list(map(int,input().split()))

m = sum(a)

a.sort()

k = m//n 
num = m%n

count = 0

for i in range(n-num) :
	count += abs(a[i]-k)
for r in range(n-num,n):
	count += abs(a[r]-k-1)


print(count//2)