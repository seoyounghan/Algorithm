a,b =map(int,input().split())
c=int(input())

result = b+c

if (b+c)>=60 :
	a = a+int(result/60)
	result = result%60
if a>23 :
	a=a-24

print(str(a)+" "+str(result))
