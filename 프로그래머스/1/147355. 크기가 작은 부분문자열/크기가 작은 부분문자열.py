# t, p : 숫자로 이루어진 문자열
# t에서 p와 길이가 같은 부분문자열 중에서,
# 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수 출력 

def solution(t, p):
    n = len(p)
    answer = 0
    
    for i in range(0, len(t)-n+1):
        if int(t[i:i+n]) <= int(p):
            answer += 1
    
    return answer
    