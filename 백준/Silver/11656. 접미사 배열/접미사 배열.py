S = input()

li = []

for i in range(0, len(S)) :
	li.append(S[-i:])

li.sort()

for k in range(len(li)) :
	print(li[k])