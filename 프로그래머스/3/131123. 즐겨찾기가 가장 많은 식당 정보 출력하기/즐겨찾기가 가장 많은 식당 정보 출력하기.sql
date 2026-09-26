-- 코드를 입력하세요
-- 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수 조회
-- 음식 종류 기준으로 내림차순 

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO AS R
WHERE R.FAVORITES = (SELECT MAX(R2.FAVORITES)
                    FROM REST_INFO AS R2
                    WHERE R.FOOD_TYPE = R2.FOOD_TYPE)
ORDER BY FOOD_TYPE DESC;