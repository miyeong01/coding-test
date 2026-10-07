# 배열의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수 구하기 
# commands : [i, j, k]를 원소로 가진 2차원 배열 
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 출력

def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        l = sorted(array[i-1:j])
        answer.append(l[k-1])
        
    return answer