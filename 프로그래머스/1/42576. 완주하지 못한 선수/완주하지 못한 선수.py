def solution(participant, completion):
    setP = set(participant)
    setC = set(completion)
    answer = ""
    
    if len(setP) == len(setC):
        participant.sort()
        completion.sort()
        for i in range(0, len(completion)):
            if participant[i] != completion[i]:
                answer = participant[i]
                break
        if answer == "":
            answer = participant[-1]
    else:
        subSet = list(setP - setC)
        answer = subSet[0]

    return answer