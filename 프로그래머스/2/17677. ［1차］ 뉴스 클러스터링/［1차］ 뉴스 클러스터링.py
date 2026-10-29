# 입력으로는 str1과 str2 두 문자열이 들어옴.
# 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만듦. 
# 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버림. 
# 대문자와 소문자 차이는 무시 
# 입력으로 들어온 두 문자열의 자카드 유사도 출력
# 유사도는 0에서 1 사이의 실수. 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력 
# 자카드 유사도 = 교집합 크기 / 합집합 크기 
# 모두 공집합일 경우에는 1

def solution(str1, str2):
    str1_set = []
    str2_set = []
    
    for i in range(len(str1) - 1):
        s = str1[i] + str1[i+1]
        if s.isalpha():
            str1_set.append(s.lower())
            
    for i in range(len(str2) - 1):
        s = str2[i] + str2[i+1]
        if s.isalpha():
            str2_set.append(s.lower())
            
    is_cnt = 0
    str2_set_cp = list(str2_set)
    for str in str1_set:
        if str in str2_set_cp:
            str2_set_cp.remove(str)
            is_cnt += 1
            
    if len(str1_set) == len(str2_set) == 0:
        jaccard = 1
    else:
        jaccard = is_cnt / (is_cnt + (len(str1_set) - is_cnt) + (len(str2_set) - is_cnt))
        
    return int(jaccard * 65536)
    