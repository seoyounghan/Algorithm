n = int(input())

num=[[0]*6 for i in range(n)]

result=[]
con=[]
for i in range(n):
	a,b,c=map(int,input().split())
	num[i][0]=a
	num[i][1]=b
	num[i][2]=c

for i in range(n) :
	for j in range(0,6):
		tmp=num[i].count(j+1)
		con.append(tmp)

	tmax=max(con)
	index=con.index(tmax)

	if tmax==3:
		result.append(10000+(index+1)*1000)
	elif tmax==2:
		result.append(1000+(index+1)*100)
	else:
		result.append(max(num[i])*100)
	con.clear()

print(str(max(result)))

	
