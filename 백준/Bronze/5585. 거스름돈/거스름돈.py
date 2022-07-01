changes = [500, 100, 50, 10, 5, 1]

money = 1000 - int(input())

count = 0

for change in changes : 
	count += money//change
	money = money%change

print(count)