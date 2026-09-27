-- 코드를 입력하세요
-- 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서
-- 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수 리스트 출력
-- 월 : 오름차순, 자동차 ID : 내림차순
-- 특정 월의 총 대여 횟수가 0이면 결과에서 제외

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE >= '2022-08-01' AND START_DATE < '2022-11-01'
AND CAR_ID IN (SELECT CAR_ID
                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                WHERE START_DATE >= '2022-08-01' AND START_DATE < '2022-11-01'
                GROUP BY CAR_ID
                HAVING COUNT(*) >= 5)
GROUP BY MONTH, CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;