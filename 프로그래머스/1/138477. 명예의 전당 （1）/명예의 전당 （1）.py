# 매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면
# 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념
# 프로그램 시작 이후 초기 k일까지는 모든 출연 가수의 점수가 명예의 전당에 오르게 됨.
# 출연 가수의 점수가 명예의 전당에 오르면 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됨. 
# k : 명예의 전당 목록의 점수의 개수
# score : 1일부터 마지막 날까지 출연한 가수들의 점수
# 매일 발표된 명예의 전당의 최하위 점수 출력

def solution(k, score):
    answer = [] # 매일 발표된 명예의 전당의 최하위 점수 
    rank = [] # 명예의 전당
    
    for s in score:
        if len(rank) < k:
            rank.append(s)
        else:
            if rank[-1] < s:
                rank[-1] = s
        rank.sort(reverse=True)
        answer.append(rank[-1])
        
    return answer
        
    