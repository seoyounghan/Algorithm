import sys
input = sys.stdin.readline

N,K = map(int, input().split())

Li = list(range(1,N+1))
Ans = []

Num = K-1

while len(Li) != 0 :
	#print(Num, len(Li))
	if Num >= len(Li):
		Num = Num%len(Li) 
	tmp = Li[Num]
	Li.remove(tmp)
	Ans.append(tmp)
	Num = Num - 1 + K
print("<",end ="")
printLi = str(Ans)[1:-1]
print(printLi + ">")