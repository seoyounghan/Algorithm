import sys
input = sys.stdin.readline

A = input()
A = A.rstrip()
Ans = 0
Cnt = 1
tmp = 0
#- 인 상태일 경우 1 아닐경우 0 
Flag = 0

def counting(Flag, Ans, tmp):
	if Flag == 1:
		Ans -= tmp
		return Ans
	else :
		Ans += tmp
		return Ans

for i in A:

	if i == "-" :
		Ans = counting(Flag,Ans,tmp)
		Flag = 1
		Cnt = 1
		tmp = 0
	elif i == "+":
		Ans =counting(Flag, Ans, tmp)
		if Flag == 1:
			Flag = 1
			Cnt = 1
			tmp = 0
		else :
			Flag = 0
			Cnt = 1
			tmp = 0
	else :
		if i != 0:
			tmp = int(i) + tmp*10
		
		#print(tmp, Cnt,Ans)

Ans = counting(Flag,Ans,tmp)
print(Ans)
