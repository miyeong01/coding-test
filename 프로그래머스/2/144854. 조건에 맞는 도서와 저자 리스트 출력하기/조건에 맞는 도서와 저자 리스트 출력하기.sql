-- 코드를 입력하세요
-- '경제' 카테고리에 속하는 도서들의 도서 id, 저자명, 출판일 리스트 출력
-- 출판일 기준으로 오름차순

SELECT BOOK_ID, AUTHOR_NAME, PUBLISHED_DATE
FROM BOOK AS A
JOIN AUTHOR AS B
ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE ASC;