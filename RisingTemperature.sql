# Write your MySQL query statement below
SELECT DISTINCT b.id
FROM weather a JOIN weather b on DATEDIFF(a.recordDate, b.recordDate) = -1
WHERE a.temperature < b.temperature;