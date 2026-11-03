# 컨테이너 벨트에서 1번 상자부터 상자를 내릴 수 있음.
# 근데 기사님이 알려준 순서에 맞게 택배상자를 실어야 함.
# 만약 컨테이너 벨트의 맨 앞에 놓인 상자가 실어야 하는 순서가 아니라면 그 상자를 실을 때까지 다른 데 보관
# 보조 컨테이너 벨트는 후입선출
# 보조 컨테이너를 이용해도 원하는 순서대로 상자를 싣지 못하면, 더 이상 상자를 싣지 않음.
# order : 기사님이 원하는 상자 순서
# 영재가 몇 개의 상자를 실을 수 있는지 출력 

def solution(order):
    container = [] # 보조 컨테이너 벨트 
    i = 0 # 기사님이 원하는 상자 몇 번째인지
    box = 1 # 지금 내릴 수 있는 상자 번호 
    answer = 0 # 영재가 싣는 상자의 개수 
    
    # order가 아니라 box가 움직이는 애
    
    while True:
        # 1. 모든 상자를 실었는가 - 그렇다면 종료
        if i >= len(order):
            return answer
        else:
            # 2. 보조 컨테이너 맨 위가 원하는 상자인가 - 맞다면 꺼내기
            if container and container[-1] == order[i]:
                container.pop()
                i += 1
                answer += 1
            else:
                # 3. 메인 벨트에 상자가 남아 있는가 - 아니면 종료
                if box > len(order):
                    return answer
                else:
                    # 4. 메인 벨트가 원하는 상자인가 - 맞으면 트럭에, 아니면 보조에 싣기 
                    if box == order[i]:
                        i += 1
                        answer += 1
                        box += 1
                    else:
                        container.append(box)
                        box += 1       