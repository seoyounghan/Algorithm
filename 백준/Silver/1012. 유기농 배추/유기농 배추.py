import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
	stack = []
	M,N,K = map(int, input().split())

	graph = []

	for _ in range(K):
		a,b = map(int, input().split())
		graph.append([b,a])

	ans = 0

	while len(graph) != 0:	
		if len(stack) == 0:
			tmp = graph.pop()
			stack.append(tmp)
			ans +=1 
		else :
			tmp = stack[-1]
			x = tmp[0]
			y = tmp[1]

			if [x-1,y] in graph:
				stack.append([x-1,y])
				graph.remove([x-1,y])
			elif [x+1,y] in graph:
				stack.append([x+1,y])
				graph.remove([x+1,y])
			elif [x,y-1] in graph:
				stack.append([x,y-1])
				graph.remove([x,y-1])
			elif [x,y+1] in graph:
				stack.append([x,y+1])
				graph.remove([x,y+1])
			else:
				stack.pop()




	print(ans)
	graph.clear()
	stack.clear()
