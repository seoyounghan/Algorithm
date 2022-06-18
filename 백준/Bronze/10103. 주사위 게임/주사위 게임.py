n=int(input())

a=100
b=100

for i in range(1,n+1) :
	na,nb=map(int,input().split())

	if na>nb :
		b-=na
	elif na<nb:
		a-=nb
	
print("%d %d"%(a,b))