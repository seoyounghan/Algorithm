n = int(input())

add1=0
add2=1

for i in range(2,n+1):
	tmp = add2
	add2 += add1
	add1 = tmp

print(add2)