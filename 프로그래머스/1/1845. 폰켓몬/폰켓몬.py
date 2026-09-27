# 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택하려 함.
# nums : N마리 폰켓몬의 종류 번호가 담긴 배열
# N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아
# 폰켓몬 종류 번호의 개수 출력

def solution(nums):
    n = len(nums)
    nums_set = set(nums)
    
    if (n//2) > len(nums_set):
        return len(nums_set)
    else:
        return n//2