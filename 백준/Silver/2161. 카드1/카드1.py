from collections import deque

N = int(input())

trashCard = []
q = deque([])
for i in range(1,N+1):
	q.append(i)

while q:
	tmp = q.popleft()
	trashCard.append(tmp)

	if q:
		q.append(q.popleft())

print(*trashCard)