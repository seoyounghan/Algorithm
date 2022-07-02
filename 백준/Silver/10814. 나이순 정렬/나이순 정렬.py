n = int(input())
dic = []

for i in range(0,n):
	a, b = input().split()
	a = int(a)

	dic.append([a,b])
	
dic.sort(key = lambda x: x[0])

for key in dic:
	print(str(key[0]) + " " + key[1])