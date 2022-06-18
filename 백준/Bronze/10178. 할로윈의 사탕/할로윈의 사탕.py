t = int(input())

for i in range(0,t) :
	c,v = map(int,input().split())

	p = c//v
	d = c%v

	print("You get %d piece(s) and your dad gets %d piece(s)."%(p,d) )