# strings : 문자열로 구성도니 리스트
# n : 정수
# 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬
def solution(strings, n):
    strings.sort(key=lambda x:(x[n], x))
    
    return strings
    