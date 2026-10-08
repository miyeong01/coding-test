# data : [code, date, maximu, remain]
# ext : 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열
# val_ext : 뽑아낼 정보의 기준값
# sort_by : 정보를 정렬할 기준이 되는 문자열
# data에서 ext값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값으로 기준으로 오름차순 정렬

def solution(data, ext, val_ext, sort_by):
    answer = []
    
    idx = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    
    for d in data:
        if d[idx[ext]] < val_ext:
            answer.append(d)
    
    answer = sorted(answer, key = lambda x:x[idx[sort_by]])
        
    return answer