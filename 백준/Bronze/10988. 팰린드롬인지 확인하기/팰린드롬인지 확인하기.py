string=input()

leng=len(string)

result =1

if len(string)%2!=0:
	tmp1 = string[:leng//2]
	tmp2 = string[leng//2+1:]
	tmp = tmp1+tmp2
	leng-=1
else :
	tmp = string

for i in range(0,leng//2):
	if tmp[i]!=tmp[leng-1-i]:
		result = 0
		break

	result = 1

print(str(result))