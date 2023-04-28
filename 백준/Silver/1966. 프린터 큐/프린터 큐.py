A = int(input())



for i in range(A):
	N,M = map(int,input().split())

	li = list(map(int,input().split()))

	count = 0
	ans = M
	flag = 1

	while flag:
		maxcount = max(li)
		tmp = li.pop(0)
		if maxcount == tmp :
			count += 1
			if ans == 0:
				print(count)
				flag = 0
		else :
			li.append(tmp)

		if ans > 0:
			ans -= 1
		else : 
			ans = len(li)-1

	li=[]