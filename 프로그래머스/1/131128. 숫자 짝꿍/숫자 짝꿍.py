# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라고 함.
# X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1
# X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0

def solution(X, Y):
    common = [] # 공통되는 숫자 넣기
    
    for i in range(9, -1, -1):
        X_count = X.count(str(i))
        Y_count = Y.count(str(i))
        count = min(X_count, Y_count)
        common.extend([str(i)] * count)
        
    if len(common) == 0:
        return "-1"
    elif ["0"] * len(common) == common:
        return "0"
    else:
        return ''.join(common)