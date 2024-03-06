import sys
input = sys.stdin.readline

S = set()

M = int(input())

for _ in range(M):
	tmp = input()

	if (tmp != "all\n") and (tmp != "empty\n") :
		a,b = tmp.split()
		b = int(b.rstrip())
	else :
		a = tmp.rstrip()

	if a == "add" :
		S.add(b)
	elif a == "remove":
		S.discard(b)
	elif a == "check":
		print(int(b in S))	
	elif a == "toggle":
		if b in S:
			S.discard(b)
		else :
			S.add(b)
	elif a == "all":
		S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

	elif a == "empty":
		S.clear()
	#print(a,b,S)


