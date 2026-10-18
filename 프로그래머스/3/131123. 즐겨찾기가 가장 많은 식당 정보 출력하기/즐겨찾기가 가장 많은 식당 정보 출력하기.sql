-- 코드를 입력하세요
SELECT I.FOOD_TYPE, I.REST_ID, I.REST_NAME, I.FAVORITES
FROM REST_INFO I
where (I.FOOD_TYPE, I.FAVORITES) in(
                                    select FOOD_TYPE, MAX(FAVORITES)
                                    from REST_INFO
                                    group by FOOD_TYPE
                                    )
order by 1 desc