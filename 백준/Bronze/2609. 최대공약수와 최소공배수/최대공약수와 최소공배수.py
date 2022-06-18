a,b=map(int,input().split())

if a<b :
	c=a
	a=b
	b=c

a1=a
b1=b


while b1!=0:
	r=a1%b1
	a1=b1
	b1=r

print(str(a1))
print(str(a*b//a1))