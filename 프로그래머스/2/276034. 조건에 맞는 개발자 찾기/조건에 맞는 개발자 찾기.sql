-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS
where SKILL_CODE & (
    SELECT CODE
    from SKILLCODES
    where NAME = 'Python')
or SKILL_CODE & (
    SELECT CODE
    from SKILLCODES
    where NAME = 'C#')
order by ID