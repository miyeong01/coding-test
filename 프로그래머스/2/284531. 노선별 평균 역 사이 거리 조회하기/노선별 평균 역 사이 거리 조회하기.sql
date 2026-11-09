-- 코드를 작성해주세요
-- 노선별로 노선, 총 누계 거리, 평균 역 사이 거리 조회
-- 총 누계 거리는 소수 둘째자리에서, 평균 역 사이 거리는 소수 셋째 자리에서 반올림, 단위 함께 출력
-- 총 누계 거리 내림차순

SELECT ROUTE, CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE,
    CONCAT(ROUND(SUM(D_BETWEEN_DIST)/COUNT(*), 2), 'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY SUM(D_BETWEEN_DIST) DESC;