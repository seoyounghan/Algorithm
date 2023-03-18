N,K = map(int, input().split())

li = []
score = [0,0,0]

for i in range(N):
	tmp = list(map(int, input().split()))
	tmp[3], tmp[0] = tmp[0], tmp[3]

	if tmp[3] == K :
		score = tmp

	li.append(tmp)

li.sort()



count = 0

for j in range(N-1, -1, -1) :
	if li[j][0] == score[0] and li[j][1] == score[1] and li[j][2] == score[2]:
		print(count)
		break
	elif li[j][3] == K :
		print(count)
		break
	else :
		count +=1


