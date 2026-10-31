-- 코드를 작성해주세요
-- 평균 길이가 33cm 이상인 물고기들을 종류별로 분류하여 잡은 수, 최대 길이, 종류 출력
-- 종류 오름차순
-- 10cm이하는 10cm로 취급하여 평균 길이 구하기

SELECT COUNT(ID) AS FISH_COUNT, MAX(COALESCE(LENGTH, 10)) AS MAX_LENGTH, FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(COALESCE(LENGTH, 10)) >= 33
ORDER BY FISH_TYPE;