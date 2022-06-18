t = int(input())

li = []
for i in range(0,t) :
	n = int(input())

	li = list(map(int,input().split()))

	print(str(sum(li)))

	li.clear()
