-- 코드를 작성해주세요
-- 아이템의 희귀도가 'RARE'인 아이템들의 모든 다음 업그레이드 아이템의
-- 아이템 ID, 아이템 명, 아이템의 희귀도 출력
-- ID 내림차순

SELECT I.ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO AS I
JOIN ITEM_TREE AS T
ON I.ITEM_ID = T.ITEM_ID
WHERE PARENT_ITEM_ID IN
    (SELECT I.ITEM_ID
    FROM ITEM_INFO AS I
    WHERE RARITY = 'RARE')
ORDER BY I.ITEM_ID DESC;