v = int(input())

string=input()

if string.count("A")>(v/2) :
	print("A")
elif string.count("B")>(v/2) :
	print("B")
else:
	print("Tie")