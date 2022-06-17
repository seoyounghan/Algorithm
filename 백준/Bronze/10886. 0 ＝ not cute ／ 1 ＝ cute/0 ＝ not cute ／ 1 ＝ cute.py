n=int(input())

a=[]

for i in range(0,n) :
	a.append(input())

if a.count("1")>(n/2) :
	print("Junhee is cute!")
else :
	print("Junhee is not cute!")