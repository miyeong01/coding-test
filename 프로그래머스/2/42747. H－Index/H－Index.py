# H-Index : 과학자의 생산성과 영향력을 나타내는 지표 = h
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면
# h의 최댓값이 이 과학자의 H-Index
# citations : 어떤 과학자가 발표한 논문의 인용 횟수
# 이 과학자의 H-Index 출력 

# h가 n보다 커질 수는 없음.

def solution(citations):
    n = len(citations)
    
    for i in range(n, -1, -1): # 몇 번 이상 인용되었는가
        h = 0 # i번 이상 인용된 논문이 몇 편인가
        for citation in citations:
            if citation >= i:
                h += 1
        if h >= i:
            return i
            
        