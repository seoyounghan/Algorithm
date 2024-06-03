X = int(input())

binX = bin(X)
count = 0

for i in binX:
	if i == "1":
		count += 1

print(count)