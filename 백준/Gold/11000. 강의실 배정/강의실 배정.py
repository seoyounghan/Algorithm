from queue import PriorityQueue, heappush, heappop
import sys

input = sys.stdin.readline

q = PriorityQueue()

n = int(input())

for i in range(0,n):
	S,T = map(int,input().split())

	q.put((S,T))

heap = [-1]

for _ in range(q.qsize()-1):
	tmp = q.get()

	if tmp[0] >= heap[0]:
		heappop(heap)
	heappush(heap,tmp[1])

print(len(heap))
