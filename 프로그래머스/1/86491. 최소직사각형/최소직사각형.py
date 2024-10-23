def solution(sizes):
    resA = 0
    resB = 0
    for a,b in sizes:
        if a<b:
            a, b = b, a
        resA = max(a, resA)
        resB = max(b, resB)
    
        
    answer = resA*resB
    return answer