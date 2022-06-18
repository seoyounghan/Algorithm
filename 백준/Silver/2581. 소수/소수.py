import math

m = int(input())
n = int(input())

array = [True for i in range(n+1)]
array[1]=False

for i in range(2, int(math.sqrt(n)) + 1):
	if array[i]==True :
		j = 2
		while i*j <= n :
			array[i * j] = False
			j += 1

add=0
for i in range(m,n+1) :
	if array[i]==True : 
		add += i

if add ==0 :
	print("-1")
else :
	print(str(add))
	for i in range(m,n+1) :
		if array[i]==True : 
			print(str(i))
			break