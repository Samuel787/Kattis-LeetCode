# Write your MySQL query statement below
with cte (Email, Counter) as (
    select Email, count(Email)
    from person
    group by Email
)

select Email
from cte
where counter > 1;
