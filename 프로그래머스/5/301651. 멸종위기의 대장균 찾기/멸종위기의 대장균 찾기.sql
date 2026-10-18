-- 코드를 작성해주세요
WITH RECURSIVE tree AS(
    select ID, PARENT_ID, 1 AS GENERATION 
    from ECOLI_DATA
    where PARENT_ID IS NULL
    
    UNION ALL

    select e.ID, e.PARENT_ID, t.GENERATION + 1
    from ECOLI_DATA e
    INNER JOIN tree t
    on e.PARENT_ID = t.ID
)

select count(*) AS COUNT, t.GENERATION
from tree t
where not exists(
    select 1
    from ECOLI_DATA child
    where child.PARENT_ID = t.ID
)
group by t.GENERATION
order by t.GENERATION