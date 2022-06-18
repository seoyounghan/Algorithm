t=int(input())

addy=0
addk=0

for i in range(0,t) :
	for j in range(0,9) :
		y,k=map(int,input().split())

		addy+=y
		addk+=k

	if addy>addk :
		print("Yonsei")
	elif addk>addy :
		print("Korea")
	else : 
		print("Draw")
	addy=0
	addk=0

