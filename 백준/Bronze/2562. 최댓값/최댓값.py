li = []

for i in range(0,9) :
	a= int(input())

	li.append(a)

result = li.index(max(li))
print(max(li))
print(str(result+1))