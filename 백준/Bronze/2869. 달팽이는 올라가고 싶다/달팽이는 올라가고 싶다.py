a,b,v = map(int,input().split())

n1 = (v-a)%(a-b)
n2 = (v-a)//(a-b)

if n1==0 :
	print(str(n2+1))

else :
	print(str(n2+2))