import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input())

findStr = "I"
ans = 0

for i in range(N):
	findStr += "OI"

StrLen = len(findStr)

for i in range(M-StrLen+1):
	if list(findStr) == S[i:i+StrLen]:
		ans+= 1
	#print(S[i:i+StrLen])
#print(findStr)
print(ans)

