n,m = map(int,input().split())
dnaList = []

for i in range(0, n):
	a = input()
	dnaList.append(a)


resultString = ""
resultCount = 0

for i in range(0,m):
	a=0
	c=0
	g=0
	t=0
	for j in range(0,n):
		if dnaList[j][i] == 'A':
			a+=1
		elif dnaList[j][i] == 'C' :
			c+=1
		elif dnaList[j][i] == 'G' :
			g+=1
		else :
			t+=1
	tmp = max(a,c,g,t)
	resultCount+=(n-tmp)
	if tmp == a:
		resultString=resultString+"A"
	elif tmp == c:
		resultString=resultString+"C"
	elif tmp == g:
		resultString=resultString+"G"
	else:
		resultString=resultString+"T"
print(resultString)
print(resultCount)
