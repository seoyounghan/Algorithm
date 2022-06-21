n = int(input())

li=[]


for i in range(n) : 
	n1,n2 = map(int,input().split())

	li.append([n1,n2])

li.sort(key=lambda x:(x[0],x[1]))


for i in range(n) :
	print("%d %d"%(li[i][0],li[i][1]))


