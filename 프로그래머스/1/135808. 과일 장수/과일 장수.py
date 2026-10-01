# 사과는 상태에 따라 1점부터 k점까지의 점수로 분류
# k점이 최상품, 1점이 최하품
# 한 상자에 m개씩 담아 포장
# 상자에 담긴 사과 중 가장 낮은 점수가 p점인 경우, 사과 한 상자의 가격은 p * m
# 과일 장수가 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익 계산
# k : 사과의 최대 점수
# m : 한 상자에 들어가는 사과의 수
# score : 사과들의 점수

def solution(k, m, score):
    apple = len(score) # 사과 개수
    score.sort(reverse=True)
    answer = 0 # 최대 이익
    
    for i in range(0, apple-m+1, m):
        answer += min(score[i:i+m]) * m
    
    return answer