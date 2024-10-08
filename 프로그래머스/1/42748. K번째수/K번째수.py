def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        
        l = array[i-1:j]
        
        l.sort()
        
        answer.append(l[k-1])
        
    return answer