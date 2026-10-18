-- 코드를 입력하세요
SELECT DATE_FORMAT(B.SALES_DATE, '%Y') as YEAR, 
       DATE_FORMAT(B.SALES_DATE, '%m') as MONTH,
       COUNT(DISTINCT A.USER_ID) as PURCHASED_USERS,
       ROUND(COUNT(DISTINCT A.USER_ID) / (SELECT COUNT(*)
                                         from USER_INFO
                                         where YEAR(JOINED) = 2021), 1) as PUCHASED_RATIO
from USER_INFO A
left join ONLINE_SALE B
on A.USER_ID = B.USER_ID
where YEAR(JOINED) = 2021 AND YEAR(SALES_DATE) is not null
group by 1, 2
order by 1, 2