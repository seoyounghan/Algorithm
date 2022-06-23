li = [31,28,31,30,31,30,31,31,30,31,30,31]

a,b = map(int,input().split())
add = b
if a!=1 :
	for i in range(0,a-1):
		add += li[i]


if add%7 == 0:
	print("SUN")
elif add%7 == 1:
	print("MON")
elif add%7 == 2:
	print("TUE")
elif add%7 == 3:
	print("WED")
elif add%7 == 4:
	print("THU")
elif add%7 == 5:
	print("FRI")
else :
	print("SAT")