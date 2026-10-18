-- 코드를 작성해주세요
select ID, 
    case
        when A.PER <= 0.25 then 'CRITICAL'
        when A.PER <= 0.5 then 'HIGH'
        when A.PER <= 0.75 then 'MEDIUM'
        else 'LOW'
    end as COLONY_NAME
from(
    select ID,
    PERCENT_RANK() OVER (order by SIZE_OF_COLONY desc) as PER
    from ECOLI_DATA
) A
order by A.ID