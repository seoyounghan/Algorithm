N, M = map(int, input().split())
Li = []
Ans = 0

def countA(i,j):
	if j+1<M :
		if Li[i][j+1] == '-':
			Li[i][j+1] = '0'
			countA(i,j+1)
def countB(i,j):
	if i+1 < N:
		if Li[i+1][j] == '|':
			Li[i+1][j] = '0'
			countB(i+1,j)

for _ in range(N) :
	Li.append(list(input()))

for i in range(N):
	for j in range(M):
		if Li[i][j] == '-':
			Li[i][j] = '0'
			Ans += 1
			countA(i,j)
			
		elif Li[i][j] == '|':
			Li[i][j] = '0'
			Ans += 1
			countB(i,j)

print(Ans)