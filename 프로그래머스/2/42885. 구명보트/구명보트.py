# 구명보트에는 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있음.
# 구명보트를 최대한 적게 사용하여 모든 사람 구출
# people : 사람들의 몸무게를 담은 배열
# limit : 구명보트의 무게 제한
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값 
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어짐. 

def solution(people, limit):
    people.sort()
    
    left = 0 
    right = len(people) - 1
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        
        answer += 1
            
    return answer