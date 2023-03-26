import sys
input = sys.stdin.readline


N = int(input())

li = []

for i in range(N):
	li.append(list(map(int,input().split())))

def secondNum(a,b,c,d):
	tmplist =[a,b,c,d]
	tmplist.sort()

	return tmplist[1]

count = N 

while 1:
	if count == 1:
		print(li[0][0])
		break
	elif count == 2:
		print(secondNum(li[0][0], li[0][1], li[1][0], li[1][1]))
		break

	abclist = [[] for i in range(count)]

	for i in range((count//2)**2):
		rowcount = i//(count//2)
		abcnum = i%(count//2)

		abclist[rowcount].append(secondNum(li[rowcount*2][abcnum*2],li[rowcount*2][abcnum*2+1],\
			li[rowcount*2+1][abcnum*2], li[rowcount*2+1][abcnum*2+1]))
	li = abclist
	count = count//2

