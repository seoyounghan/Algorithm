t= int(input())

al={}


for i in range(0,t) :
	n = int(input())
	for j in range(0,n) :
		a,b=input().split()
		b=int(b)
		al[b]=a

	tmp = max(al.keys())
	print(al[tmp])

	al.clear()
