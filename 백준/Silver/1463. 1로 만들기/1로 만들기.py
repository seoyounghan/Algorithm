N = int(input())

li = [N+1]*(N+1) 

queue = [N]
li[N] = 0

while li[1] == N+1:
	curr = queue.pop(0)
	curr_count = li[curr]

	if curr % 3 == 0 and li[curr//3] == N+1:
		queue.append(curr // 3)
		li[curr//3] = curr_count + 1
	if curr % 2 == 0 and li[curr//2] == N+1:
		queue.append(curr // 2)
		li[curr//2] = curr_count + 1
	if li[curr-1] == N+1:
		queue.append(curr-1)
		li[curr-1] = curr_count + 1

print(li[1])