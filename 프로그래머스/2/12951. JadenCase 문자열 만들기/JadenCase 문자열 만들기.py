# 1번째 풀이(런타임 에러)
def solution(s):
    string = list(s.split(" "))
    answer = []
    
    for alp in string:
        alp = alp[0].upper() + alp[1:].lower()
        answer.append(alp)
    return ' '.join(answer)

# 2번째 풀이
def solution(s):
    string = list(s.split(" "))
    answer = []
    
    for a in string:
        answer.append(a.capitalize())
    return ' '.join(answer)

# 숏코딩
def solution(s):
    return ' '.join([a.capitalize() for a in list(s.split(" "))])