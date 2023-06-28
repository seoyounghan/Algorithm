N = int(input())	#크레인 수
crane = list(map(int,input().split()))
M = int(input())	#박스 수
box = list(map(int,input().split()))

crane.sort(reverse=True)
box.sort()

time = 0


if max(crane) < max(box):
	print(-1)
	exit()

while len(box) > 0:
	for i in crane:
		if len(box) == 0:
			break
		
		j = len(box)-1
		for j in range(len(box)-1,-1,-1):
			if i >= box[j]:
				box.pop(j)	
				break
			




		
	time += 1

print(time)