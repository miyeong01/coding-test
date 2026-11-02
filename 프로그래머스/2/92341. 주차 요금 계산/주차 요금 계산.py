# 차랑별 주차 요금 계산 
# 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
# 누적 주차 시간이 기본 시간 이하라면, 기본 요금 청구
# 기본 시간 초과하면, 기본 요금에 더해서, 초과한 시간에 대해 단위 시간마다 단위 요금 청구
# 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림
# fees : 주차 요금을 나타내는 정수 배열, [기본 시간, 기본 요금, 단위 시간, 단위 요금]
# records : 자동차의 입/출차 내역을 나타내는 문자열 배열, "시각 차량번호 내역"
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 출력 

import math

def solution(fees, records):
    cars = {} # 차량번호 : [주차 시간, 들어온 시간]
    park = [] # 현재 주차장에 있는 차
    charge = []
    
    for record in records:
        time, number, state = record.split(" ")
        hour, minute = time.split(":")
        mm_park = int(hour) * 60 + int(minute) # 주차 시간 분으로 변환
        
        if state == "IN":
            park.append(number)
            if number not in cars:
                cars[number] = [0, 0]
            cars[number][1] = mm_park
        else:
            cars[number][0] += mm_park - cars[number][1]
            park.remove(number)
            
    if park:
        for p in park:
            cars[p][0] += 1439 - cars[p][1]
            
    for car in cars:
        if cars[car][0] <= fees[0]:
            charge.append([car, fees[1]])
        else:
            charge.append([car, fees[1] + math.ceil((cars[car][0] - fees[0]) / fees[2]) * fees[3]])
            
    return [c[1] for c in sorted(charge)]