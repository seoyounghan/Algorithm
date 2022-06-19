a=[]

def func(n1,n2,n3) :
	if n1**2 == n2**2+n3**2 :
		print("right")
	else : 
		print("wrong")



while 1 :
	a=list(map(int,input().split()))

	if (a[0]==0)& (a[1]==0)&(a[2]==0) :
		break

	n1=max(a)

	if a.index(n1)==0 :
		func(n1,a[1],a[2])
	elif a.index(n1)==1 :
		func(n1,a[0],a[2])
	else : 
		func(n1,a[0],a[1])


	a.clear()

