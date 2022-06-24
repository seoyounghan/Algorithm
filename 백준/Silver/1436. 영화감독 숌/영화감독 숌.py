n = int(input())

count = 0
num= 666

while 1:
	if str(num).find("666") != -1 :
		count+=1
	if count == n :
		break
	num+=1
print(num)