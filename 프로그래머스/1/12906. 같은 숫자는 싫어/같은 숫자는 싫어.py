# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
# 제거된 후 남은 수들을 반환할 때는 순서 유지

def solution(arr):
    answer = []
    
    for n in arr:
        if not answer or answer[-1] != n:
            answer.append(n)
    
    return answer
            