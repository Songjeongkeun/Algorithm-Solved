-- 코드를 작성해주세요
SELECT B.ITEM_ID, A.ITEM_NAME, A.RARITY
from ITEM_INFO A
left
join ITEM_TREE B
on A.ITEM_ID = B.ITEM_ID
where B.PARENT_ITEM_ID in(
    SELECT ITEM_ID
    from ITEM_INFO
    where RARITY = 'RARE')
order by B.ITEM_ID desc