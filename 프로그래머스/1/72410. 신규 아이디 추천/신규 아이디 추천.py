# 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
# 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램 개발
# 아이디의 길이는 3자 이상 15자 이하
# 아이디는 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 문자만 사용할 수 있음.
# 마침표는 처음과 끝에 사용할 수 없으며 연속으로도 사용 X
# new_id : 신규 유저가 입력한 아이디
# "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디 출력 

def solution(new_id):
    # 1단계 : 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계 : 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    # 3단계 : 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
    filtered_id = ''
    check = 0 # 마침표였으면 1로 바꾸고 1이면 더이상 추가 ㄴㄴ
    for n in new_id:
        if n.isalnum() or n in '-_':
            filtered_id += n
            check = 0
        elif n == '.':
            if check == 0:
                check += 1
                filtered_id += n
            else:
                pass
            
    # 4단계 : 마침표가 처음이나 끝에 위치한다면 제거
    filtered_id = filtered_id.strip('.')
        
    # 5단계 : 빈 문자열이면, 'a' 대입
    if len(filtered_id) == 0:
        filtered_id = 'a'
        
    # 6단계 : 길이가 16자 이상이라면 첫 15개의 문자를 제외한 나머지는 전부 제거
    # 제거 후 마침표가 끝에 위치한다면 그것도 제거
    if len(filtered_id) >= 16:
        filtered_id = filtered_id[:15]
        if filtered_id[-1] == '.':
            filtered_id = filtered_id[:14]
            
    # 7단계 : 2자 이하이면 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 추가
    if len(filtered_id) <= 2:
        last = filtered_id[-1]
        while len(filtered_id) < 3:
            filtered_id += last
    
    return filtered_id