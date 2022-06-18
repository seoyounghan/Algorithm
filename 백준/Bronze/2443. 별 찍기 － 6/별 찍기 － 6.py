n = int(input())

for i in range(1,1+n) :
	for j in range(0,i-1) :
		print(" ",end = '')
	for j in range(0,2*n-(i*2-1)) :
		print("*",end='')

	print("")
    