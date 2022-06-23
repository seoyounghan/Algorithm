t = int(input())

for i in range(0,t) :
	h,w,n = map(int,input().split())

	a=n//h
	b=n%h

	if b == 0 :
		b=h
		a=a-1


	result= (b)*100+(a+1)
	print("%d"%(result))