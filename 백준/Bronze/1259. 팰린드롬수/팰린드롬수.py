while 1:
	a=input()
	if a == "0" :
		break
	if len(a) == 1 :
		print("yes")

	if len(a)%2 != 0 :
		a = a[:len(a)//2] + a[len(a)//2 +1:]

	for i in range(0,len(a)//2) : 
		if a[i] != a[len(a)-1-i] :
			print("no")
			break
		if i == len(a)//2 -1 :
			print("yes")