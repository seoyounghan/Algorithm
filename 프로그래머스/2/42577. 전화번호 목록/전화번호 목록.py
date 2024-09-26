def solution(phone_book):
    answer = True
    phone_book.sort()
    prev = "  "
    
    for i in phone_book:
        if i.startswith(prev):
            answer = False
            break
        prev = i
    return answer