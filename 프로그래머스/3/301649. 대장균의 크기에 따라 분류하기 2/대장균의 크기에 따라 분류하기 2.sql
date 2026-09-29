-- 코드를 작성해주세요 --
-- 대장균 개체의 크기 내림차순
-- 상위 0% ~ 25%를 'CRITICAL', 50% 이하는 'HIGH', 75% 이하는 'MEDIUM', 100% 이하는 'LOW'
-- 대장균 개체의 ID와 분류된 이름 출력
-- 결과는 개체 ID 오름차순

SELECT ID,
    CASE NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC)
        WHEN 1 THEN 'CRITICAL'
        WHEN 2 THEN 'HIGH'
        WHEN 3 THEN 'MEDIUM'
        WHEN 4 THEN 'LOW'
    END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID ASC;