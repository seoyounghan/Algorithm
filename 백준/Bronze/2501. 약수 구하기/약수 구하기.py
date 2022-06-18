n,k=map(int,input().split())

li=[]
count=0

for i in range(1,n+1) :
	if n%i==0 :
		li.append(i)
		count+=1
if count<k :
	print("0")
else : 
	print(str(li[k-1]))
    