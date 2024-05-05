# 1번째 풀이(런타임 에러)
def solution(s):
    string = list(s.split())
    answer = []
    
    for alp in string:
        alp = alp[0].upper() + alp[1:].lower()
        answer.append(alp)
        
    return ' '.join(answer)

# 2번째 풀이(그냥 틀림)
'''
1) s.split()
2) s.split(" ")

둘 모두 공백 문자를 기준으로 문자를 분리하는 것은 맞음
1)의 경우 연속된 공백 문자는 무시됨
2)의 경우 공백 문자 사이 추가 공백도 모두 포함하여 문자열 분리

즉, 'a____a'가
['a', 'a'] 또는 ['a', '_', '_', '_', 'a']로 분리되는 것의 차이

'''
def solution(s):
    string = list(s.split()) # -> s.split(" "). "문제 조건: 공백문자가 연속해서 나올 수 있습니다."
    answer = []
    
    for a in string:
        answer.append(a.capitalize()) # 반례: 'aaaAA'
        
    return ' '.join(answer)

# 3번째 풀이(런타임 에러)
def solution(s):
    answer = ''
    words = s.split(" ")    
    for i, word in enumerate(words):
        if word and not word.isdigit(): 
            f_letter = word[0].upper()
            rest_word = word[1:].lower()
            words[i] = f_letter + rest_word
    return ' '.join(words)


# # 숏코딩
# def solution(s):
#     return ' '.join([a[0].upper()+a[1:].lower() for a in list(s.split(" "))])