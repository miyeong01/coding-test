# HEAD는 숫자가 아닌 문자, 최소한 한 글자 이상
# NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자
# TAIL은 나머지 부분, 숫자가 다시 나타날 수도 있고, 아무 글자도 없을 수도 있음. 
# 우선 HEAD 부분을 기준으로 사전 순으로 정렬
# 문자열 비교 시 대소문자 구분 X
# 파일명의 HEAD 부분이 같으면 NUMBER의 숫자 순으로 정렬. 숫자 앞의 0은 무시
# HEAD랑 NUMBER가 같으면 원래 입력에 주어진 순서 유지 

def solution(files):
    sorted_files = []
    
    for file in files:
        head = ""
        i = 0
        while (not file[i].isdigit()):
            head += file[i]
            i += 1
        
        number = ""
        j = i
        while (j < len(file) and file[j].isdigit() and len(number) < 5):
            number += file[j]
            j += 1
        
        sorted_files.append([file, head, number])
    
    sorted_files = sorted(sorted_files, key=lambda x : (x[1].lower(), int(x[2])))
    
    return [file[0] for file in sorted_files]
        
    
        
        
        