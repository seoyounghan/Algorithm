li=[]
while 1:
	n=int(input())
	if n==(-1) :
		break

	for i in range(1,(n//2)+2) :
		if (n%i)==0 : 
			li.append(i)

	if sum(li)== n :
		print (str(n)+" = ",end='')
		for i in range(0,len(li)-1) :
			print(str(li[i])+" + ",end='')
		print(str(li[-1]))
	else :
		print(str(n)+" is NOT perfect.")

	li.clear()
