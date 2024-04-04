import sys
input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())

dice = [0, 0, 0, 0, 0, 0]

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
mapList = []

dx = [0, 0, 0, -1 , 1]
dy = [0, 1, -1, 0, 0]

def changeDice(num0,num1,num2,num3,num4,num5):
	dice[0] = num0
	dice[1] = num1
	dice[2] = num2
	dice[3] = num3
	dice[4] = num4
	dice[5] = num5


for i in range(N): 
	tmp = list(map(int, input().split()))
	mapList.append(tmp)

throwList = list(map(int, input().split()))

for i in throwList:

	X = dx[i] + x 
	Y = dy[i] + y
	#print(i,X,Y)
	if X >=N or Y >= M or X <0 or Y <0:
		#print(i,X,Y)
		continue
	else :
		x = X 
		y = Y

	if i == 1:
		changeDice(dice[3],dice[1],dice[0],dice[5],dice[4],dice[2])

	elif i ==2:
		changeDice(dice[2],dice[1],dice[5],dice[0],dice[4],dice[3])

	elif i == 3:
		changeDice(dice[4],dice[0],dice[2],dice[3],dice[5],dice[1])

	elif i == 4:
		changeDice(dice[1],dice[5],dice[2],dice[3],dice[0],dice[4])

	if mapList[x][y] == 0:
		mapList[x][y] = dice[5]
	else:
		dice[5] = mapList[x][y]
		mapList[x][y] = 0
	print(dice[0])

