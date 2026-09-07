# 문자열 s가 주어졌을 때, s이 각 위치마다 자신보다 앞에 나왔으면서,
# 자신과 가장 가까운 곳에 있는 같은 글자가 몇 칸 앞에 있는가
# 자신의 앞에 같은 글자가 없으면 -1 출력

def solution(s):
    answer = [] # 각 문자열 별로 자신과 가장 가까운 곳에 있는 글자가 몇 칸 앞에 있는지
    order = {} # 문자열 : 몇 번째에 나왔는지, 업데이트 됨
    
    for i in range(len(s)):
        if s[i] in order:
            answer.append(i - order[s[i]])
        else:
            answer.append(-1)
        order[s[i]] = i
        
    return answer