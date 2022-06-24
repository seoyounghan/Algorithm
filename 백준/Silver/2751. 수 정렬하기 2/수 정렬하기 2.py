import sys
n = int(input())
li=[]
for i in range(n) :
	li.append(int(sys.stdin.readline()))


li = list(set(li))
li.sort()
li = map(str,li)


print("\n".join(li))