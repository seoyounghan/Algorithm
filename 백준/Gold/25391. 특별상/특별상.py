import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
li=[]


for i in range(N):
	li.append(list(map(int,input().split())))
li.sort(key = lambda x:x[1])

ans = 0
li1 = []

for i in range(N-1,N-K-1,-1):
	tmp = li.pop()
	ans += tmp[0]
li.sort(reverse=True)


count = 0
while count<M:
	ans += li[count][0]
	count += 1
print(ans)