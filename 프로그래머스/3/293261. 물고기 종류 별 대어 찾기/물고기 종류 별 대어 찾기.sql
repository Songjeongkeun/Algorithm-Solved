-- 코드를 작성해주세요
select F.ID, I.FISH_NAME, F.LENGTH
from FISH_INFO F
inner join FISH_NAME_INFO I
ON F.FISH_TYPE = I.FISH_TYPE
where (F.FISH_TYPE, F.LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH)
                                 from FISH_INFO
                                 GROUP BY FISH_TYPE)
order by 1