import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
li = []
ans = 1
q = PriorityQueue()
q.put(0)

for i in range(N) : 
	a, b, c = map(int, input().split())
	tmp = [b, c, a]
	li.append(tmp)

li.sort()

for i in li :
	start = i[0]
	end = i[1]
	num = i[2]
	
	smallEnd = q.get()

	if start >= smallEnd :
		q.put(end)
	else :
		ans += 1
		q.put(end)
		q.put(smallEnd)


print(ans)