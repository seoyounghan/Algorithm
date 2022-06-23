n,m =map(int,input().split())

li =[]
a="WBWBWBWB"
b="BWBWBWBW"

for i in range(n) :
	li.append(input())

countlist = []
#print(li)

def counting(x,y) :
	count = 0
	for i in range(y,y+8):
		for j in range(x,x+8) : 
			#print("%d %d"%(x,y))
			if j==0 or j%2==0 :
				if a[i-y] != li[j][i] :
					count +=1 

			else :
				if b[i-y] != li[j][i] :
					count +=1


	return count



for i in range(0, n-7) :
	for j in range(0, m-7) :
		count = counting(i,j)
		#print(str(count))
		countlist.append(count)

maxc = 64 - max(countlist)
minc = min(countlist)

if maxc <= minc :
	print(str(maxc))
else :
	print(str(minc))

