import sys
import math

input = sys.stdin.readline

N = int(input())
array = [1 for i in range(N + 1)] 
array[0] = 0
array[1] = 0
#1은 소수
#0은 소수 아님

for i in range(2, int(math.sqrt(N)) + 1):
    if array[i] == 1: 
        j = 2
        while i * j <= N:
            array[i * j] = 0
            j += 1
primes=[i for i in range(N+1) if array[i] == 1]
top = len(primes)
bottom = 0
magicNum = 5000001

while 1:
	#print(top,bottom)
	if top < bottom:
		break
	mid = (top+bottom)//2

	print(f'? {primes[mid]}')

	sys.stdout.flush() 

	ans = input().rstrip()
	#print(ans)

	if ans == "1":
		# mid 위를 찾아보아야
		bottom = mid + 1
	elif ans == "0":
		# mid 아래쪽 찾아보기 or 해당이 답일수도? => 일단 저장 필요!
		top = mid - 1
		magicNum = min(primes[mid], magicNum)
print(f'! {magicNum}')
sys.stdout.flush()
exit()