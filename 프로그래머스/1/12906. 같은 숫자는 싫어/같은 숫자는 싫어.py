def solution(arr):
    answer = [arr[0]]
    prev = arr[0]
    
    for i in arr:
        if prev != i:
            answer.append(i)
        prev= i
    return answer