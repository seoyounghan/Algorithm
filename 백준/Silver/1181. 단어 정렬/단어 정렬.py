n = int(input())

li = []

for i in range(0,n) :
	li.append(input())

li=list(set(li))
li.sort()
li.sort(key=len)

for i in range(0,len(li)) : 
	print(li[i])