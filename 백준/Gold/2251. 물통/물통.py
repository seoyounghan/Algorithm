import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())
stack = [(0,0,C)]
visited = [(0,0,C)]

Ans = [C]

def check(a,b,c) :
	if (a,b,c) not in visited and (a+b+c == C):
		stack.append((a,b,c))
		visited.append((a,b,c))
		if a == 0 and (c not in Ans) :
			Ans.append(c)
			#print(a,b,c)

while stack:
	tmp = stack.pop()
	#A를 붓기
	if A != 0:
		#B가 꽉 찬 경우
		if (tmp[1] + tmp[0]) >= B :
			check(tmp[1]+tmp[0]-B,B,tmp[2])
		else :
			check(0,tmp[0]+tmp[1],tmp[2])

		if (tmp[0] + tmp[2]) >= C :
			check(tmp[0]+tmp[2]-C,tmp[1],C)
		else :
			check(0,tmp[1],tmp[0]+tmp[2])

	if B != 0:
		if (tmp[1] + tmp[2]) >= C:
			check(tmp[0],tmp[1]+tmp[2]-C,C)
		else :
			check(tmp[0],0,tmp[1]+tmp[2])

		if (tmp[1] + tmp[0]) >= A:
			check(A,tmp[0]+tmp[1]-A,tmp[2])
		else :
			check(tmp[0]+tmp[1],0,tmp[2])


	if C != 0:
		if (tmp[0] + tmp[2]) >= A:
			check(A,tmp[1],tmp[0]+tmp[2]-A)
		else :
			check(tmp[0]+tmp[2],tmp[1],0)

		if (tmp[0] + tmp[1]) >= B:
			check(tmp[0],B,tmp[0]+tmp[1]-B)
		else :
			check(tmp[0],tmp[0]+tmp[1],0)
Ans.sort()
for i in Ans:
	print(i,end=" ")
