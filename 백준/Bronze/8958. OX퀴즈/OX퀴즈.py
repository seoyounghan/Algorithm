n = int(input())
add = 0
for i in range(0,n) :
	string = input()

	count=0
	for j in range(0,len(string)):
		if string[j]=="O" :
			count+=1
		else :
			if(count>=1):
				add+=((count+1)*count//2)
				count=0
	if(count>=1):
		add+=((count+1)*count//2)
		count=0

	print(str(add))
	add = 0

