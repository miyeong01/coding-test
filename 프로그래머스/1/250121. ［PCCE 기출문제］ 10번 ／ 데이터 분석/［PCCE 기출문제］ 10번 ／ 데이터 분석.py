# data : [code, date, maximu, remain]
# ext : 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열
# val_ext : 뽑아낼 정보의 기준값
# sort_by : 정보를 정렬할 기준이 되는 문자열
# data에서 ext값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값으로 기준으로 오름차순 정렬

def solution(data, ext, val_ext, sort_by):
    answer = []
    
    for d in data:
        if ext == "code":
            if d[0] < val_ext:
                answer.append(d)
        elif ext == "date":
            if d[1] < val_ext:
                answer.append(d)
        elif ext == "maximum":
            if d[2] < val_ext:
                answer.append(d)
        else:
            if d[3] < val_ext:
                answer.append(d)
                
    if sort_by == "code":
        answer = sorted(answer, key = lambda x:x[0])
    elif sort_by == "date":
        answer = sorted(answer, key = lambda x:x[1])
    elif sort_by == "maximum":
        answer = sorted(answer, key = lambda x:x[2])
    else:
        answer = sorted(answer, key = lambda x:x[3])
        
    return answer