import numpy
def solution(N, stages):
    tmp = [0]*N
    tmp2 = []
    stages.sort()
    
    prev = 0
    for index, a in enumerate(stages):
        if prev != a and a < N+1:
            tmp[a-1] = stages.count(a) / (len(stages) - index)
            
            
        prev = a
    
    for i, a in enumerate(tmp):
        tmp2.append([i+1, a])
        
    ans = sorted(tmp2, key = lambda x: (-x[1], x[0]))
    
    answer = []
    
    for i in ans:
        answer.append(i[0])
        
    return answer