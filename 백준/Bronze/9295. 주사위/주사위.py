t=int(input())

li=[]

for i in range(0,t) :
	a,b = map(int,input().split())
	li.append(a+b)

for i in range(1,t+1) :
	print("Case %d: %d"%(i,li[i-1]))
