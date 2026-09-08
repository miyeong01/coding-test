# 모든 음식의 스코빌 지수를 K 이상으로 만들거임.
# 새로운 음식 = 스코빌 지수가 가장 낮은 음식의 지수 + (두 번째로 낮은 거 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수 
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1 출력 

import heapq

def solution(scoville, K):
    answer = 0 # 음식 섞어야 하는 최소 횟수
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) >= 2:
            first = heapq.heappop(scoville) # 가장 낮은 거
            second = heapq.heappop(scoville) # 두번째로 낮은 거

            new = first + second * 2 # 새로운 음식 
            heapq.heappush(scoville, new)

            answer += 1
        else:
            return -1
    
    return answer