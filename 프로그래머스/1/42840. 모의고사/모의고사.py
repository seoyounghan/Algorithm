def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = [0, 0, 0, 0]
    answer = []
    
    for i in range(0, len(answers)):
        if supo1[i%5] == answers[i]:
            ans[1] += 1
        if supo2[i%8] == answers[i]:
            ans[2] += 1
        if supo3[i%10] == answers[i]:
            ans[3] += 1
    maxAns = max(ans)
    for i in range(1, 4):
        if ans[i] == maxAns:
            answer.append(i)
    return answer