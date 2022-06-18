n = int(input())

li = []

li= list(map(int,input().split()))

maxi = max(li)

for i in range(0,n) :
	li[i] = li[i]/maxi*100

result = sum(li)/n
print(str(result))