-- 코드를 작성해주세요
select A.ID
from ECOLI_DATA A
join ECOLI_DATA B on A.PARENT_ID = B.ID
join ECOLI_DATA C on B.PARENT_ID = C.ID
where C.PARENT_ID is NULL
order by A.ID asc