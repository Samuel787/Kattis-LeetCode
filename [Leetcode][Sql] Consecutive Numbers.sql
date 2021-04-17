# Write your MySQL query statement below
select distinct a.num as ConsecutiveNums
from logs a join logs b on a.id + 1 = b.id and a.num = b.num
join logs c on a.id + 2 = c.id and a.num = c.num;