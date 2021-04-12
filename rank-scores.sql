# Write your MySQL query statement below

# Solution 1
select score, (select count(distinct score) from scores s1 where s1.score >= s2.score) as "Rank"
from scores s2
order by score desc;

# Solution 2
select score, dense_rank() over (order by Score desc) as "Rank" from scores

