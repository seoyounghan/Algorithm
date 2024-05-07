A = int(input())
B = int(input())
C = int(input())

ans = A*B*C 

res = str(ans)

for i in range(0, 10):
	strI = str(i)

	print(res.count(strI))