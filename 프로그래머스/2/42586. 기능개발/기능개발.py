import math
def solution(progresses, speeds):
    answer = [1]
    for i in range(0, len(progresses)):
        progresses[i] = math.ceil((100 - progresses[i])/speeds[i])
    #print(progresses)
    n = 0
    tmp = progresses[0]
    for i in range(1, len(progresses)):
        if progresses[i] <= tmp:
            answer[n] += 1
        else:
            tmp = progresses[i]
            answer.append(1)
            n+=1
    return answer