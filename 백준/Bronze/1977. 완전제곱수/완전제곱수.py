import math
import sys

m=int(input())
n=int(input())

m1=math.ceil(math.sqrt(m))
n1=math.floor(math.sqrt(n))

add = 0

if m1>=n1:
	if math.pow(m1,2)==m :
		print(str(m))
		print(str(m))
	elif math.pow(n1,2)==n :
		print(str(n))
		print(str(n))
	else :
		print(-1)
else :
	for i in range(m1,n1+1) :
		add += math.pow(i,2)

	print(str(int(add)))
	print(str(int(math.pow(m1,2))))


