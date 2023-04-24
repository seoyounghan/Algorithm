from queue import Queue

N = int(input())

li = Queue()

for i in range(N):
	li.put(i+1)

while  li.qsize()>1:
	li.get()
	li.put(li.get())


print(li.get())