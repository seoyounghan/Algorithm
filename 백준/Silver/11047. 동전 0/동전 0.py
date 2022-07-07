import sys
n,k = map(int, input().split())

coinList = []

for i in range(0,n) :
	a = int(input())

	if a <= k :
		coinList.append(a)

coinList.reverse()
result = 0

for i in coinList :
	if k >= i :
		result += k//i
		k = k%i
		
	if k == 0 :
		 break

print(result)