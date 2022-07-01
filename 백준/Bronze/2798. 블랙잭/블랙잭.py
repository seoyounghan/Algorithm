n,m = map(int,input().split())
li = list(map(int,input().split()))

maxlist=[]

li.sort(reverse=True)

for i in range(0,n) :
	a = li[i]
	for j in range(i+1, n):
		b = li[j]
		for h in range(j+1,n):
			c = li[h]
			if a+b+c <= m :
				maxlist.append(a+b+c)

print(max(maxlist))