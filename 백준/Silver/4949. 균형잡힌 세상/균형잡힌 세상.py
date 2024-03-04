tok = 1

while tok :
	A = input()
	
	if A == ".":
		tok = 0
		break
	ans = list(A)
	li = []
	anstok = 0
	for i in ans :
		if anstok == 1:
			break
		if i == "[" or i == "(":
			li.append(i)
		elif len(li)>=1 and i == ")":
			tmp = li.pop()
			if tmp != "(" :
				print("no")
				anstok = 1
		elif len(li)>=1 and i == "]":
			tmp = li.pop()
			if tmp != "[" :
				print("no")
				anstok = 1
		elif len(li) <= 0 and (i == ")" or i=="]") :
				print("no")
				anstok = 1
	if anstok == 1:
		continue				
	elif len(li) == 0:
		print("yes")
	else :
		print("no")