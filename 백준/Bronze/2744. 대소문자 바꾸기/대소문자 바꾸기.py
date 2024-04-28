inputStr = input()
res = ""

for i in inputStr:
	if i.isupper():
		res += i.lower()
	else:
		res += i.upper()

print(res)