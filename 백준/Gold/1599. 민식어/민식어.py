import sys
input = sys.stdin.readline

# a b k d e g h i l m n ng o p r s t u w y

minSick = ["a", "b", "k", "d", "e", "g", "h", "i", "l", "m", "n", "ng", "o", "p", "r", "s", "t", "u", "w", "y"]

N = int(input())
inputNumList = [[] for _ in range(N)]
inputList = []

for i in range(N):
	tmp = input().rstrip()
	inputList.append(tmp)

	num = 0

	while num < len(tmp):
		if inputList[i][num] == "n" and (num!= len(tmp)-1) and inputList[i][num+1] == "g":
			inputNumList[i].append(minSick.index("ng"))
			num += 2
		else:
			inputNumList[i].append(minSick.index(inputList[i][num]))
			num += 1

		# if num == len(tmp):
		# 	inputList[i][num].append(i)

value = sorted(inputNumList, reverse=False)
index = sorted(range(len(inputNumList)), key=lambda k: inputNumList[k], reverse=False)

for i in index:
	print(inputList[i])





