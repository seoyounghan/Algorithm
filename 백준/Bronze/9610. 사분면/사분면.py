n = int(input())

q1=0
q2=0
q3=0
q4=0
ax=0

for i in range(0,n) :
	a,b = map(int,input().split())

	if (a==0) | (b==0) :
		ax+=1
	elif a>0 :
		if b>0 :
			q1+=1
		else :
			q4+=1
	else :
		if b>0 :
			q2+=1
		else :
			q3+=1

print("Q1: "+str(q1))
print("Q2: "+str(q2))
print("Q3: "+str(q3))
print("Q4: "+str(q4))
print("AXIS: "+str(ax))


