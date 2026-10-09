-- 코드를 입력하세요
-- 공간을 둘 이상 등록한 사람을 헤비 유저
-- 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회

SELECT *
FROM PLACES
WHERE HOST_ID IN 
    (SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(*) >= 2)
ORDER BY ID;