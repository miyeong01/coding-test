-- 코드를 입력하세요
-- 만원 단위의 가격대 별로 상품 개수 출력
-- 가격대 정보는 각 구간의 최소금액으로 표시
-- 가격대를 기준으로 오름차순

SELECT TRUNCATE(PRICE, -4) AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP;