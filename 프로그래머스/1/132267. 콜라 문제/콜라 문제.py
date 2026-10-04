# a : 빈 병
# b : 빈 병 a개 가져다줬을 때 주는 콜라 개수
# n : 가져다줄 콜라 개수
# 보유 중인 빈 병이 a개 미만이면, 빈 병을 받을 수 없음.
# 상빈이가 받을 수 있는 콜라의 병 수 출력

def solution(a, b, n):
    answer = 0 # 상빈이가 받을 수 있는 콜라 개수

    while n >= a:
        empty = (n // a) * b # n개 가져다주면 받는 빈 병 개수
        answer += empty
        n = n - (n // a) * a + empty
        
    return answer
        