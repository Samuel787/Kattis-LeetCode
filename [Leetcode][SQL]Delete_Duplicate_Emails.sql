# Write your MySQL query statement below

DELETE q
FROM Person p join Person q
WHERE p.Email = q.Email AND p.Id < q.Id