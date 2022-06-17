a=input()

csame=0
cdif=1

for i in range(0,len(a)-1):
	if a[i]==a[i+1] :
		csame+=1
	else :
		cdif+=1

result=csame*5+cdif*10
print(str(result))