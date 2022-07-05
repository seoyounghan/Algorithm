n = int(input())

li = list(map(int,input().split()))

li.sort()

countli = []

result = 0
count = 1

for i in range(0, n) :
	for j in range(0, i+1) :
		result += li[j]
	countli.append(result)
	result = 0


print(sum(countli))