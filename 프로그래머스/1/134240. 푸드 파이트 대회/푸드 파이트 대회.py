# 한 선수는 제일 왼쪽에 있는 음식부터 오른쪽으로,
# 다른 선수는 제일 오른쪽에 있는 음식부터 왼쪽으로
# 중앙에는 물을 배치하고, 물을 먼저 먹는 선수가 승리함.
# food : 수웅이가 준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열
# food[i] : i번 음식의 수
# food[0] : 수웅이가 준비한 물의 양, 항상 1
# 대회를 위한 음식의 배치를 나타내는 문자열 출력 

def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        n = food[i] // 2
        answer += str(i) * n
        
    answer += '0'
    
    return answer + answer[-2::-1]