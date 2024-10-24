def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    lost_filtered = [i for i in lost if i not in reserve]
    reserve_filtered = [j for j in reserve if j not in lost]
    
    answer = n - len(lost_filtered)
    
    for i in lost_filtered:
        for j in reserve_filtered: 
            if j - 1 == i or j + 1 == i:  
                answer += 1
                reserve_filtered.remove(j)
                break 

    return answer
