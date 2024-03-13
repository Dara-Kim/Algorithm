def solution(s):
    answer = s.split()
    answer = [int(i) for i in answer]
            
    return str(min(answer)) + ' ' + str(max(answer))