n=int(input())

al = {}

for i in range(0,n) :
	p = int(input())
	for j in range(0,p) :
		b,a=input().split()

		b=int(b)

		al[b]=a

	tmp = max(al.keys())
	print(al[tmp])

	al.clear()
