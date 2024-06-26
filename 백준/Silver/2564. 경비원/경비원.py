W, H = map(int, input().split())

N = int(input())

li = []

res = 0

for i in range(N):
	d, num = map(int, input().split())
	li.append((d,num))

prevD, prevNum = map(int, input().split())

for (d, num) in li:	
	if prevD == d:
		res += abs(num-prevNum)
	elif (prevD == 1 and d ==2) or (prevD == 2 and d ==1):
		res += (H + min(prevNum+num, 2*W-prevNum-num))
	elif (prevD == 3 and d ==4) or (prevD == 4 and d ==3):
		res += (W + min(prevNum+num, 2*H-prevNum-num))
	elif (prevD == 1 and d ==3) or (prevD == 3 and d ==1):
		res += (num + prevNum)
	elif prevD == 3 and d ==2:
		res += (H-prevNum+num)
	elif d == 3 and prevD == 2:
		res += (H+prevNum-num)
	elif (prevD == 2 and d ==4) or (prevD == 4 and d ==2):
		res += (H+W-prevNum-num)
	elif prevD == 1 and d ==4:
		res += (W-prevNum+num)
	elif prevD == 4 and d == 1:
		res += (H+prevNum-num)

	#print(res)

print(res)