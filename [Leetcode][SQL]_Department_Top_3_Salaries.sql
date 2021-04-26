# Write your MySQL query statement below

SELECT d.Name AS "Department", f.Name AS "Employee", f.Salary as "Salary"
FROM (SELECT e.Name, e.Salary, e.DepartmentId, DENSE_RANK() OVER(PARTITION BY e.DepartmentId ORDER BY e.Salary DESC) AS "Rank"
FROM Employee e) f JOIN Department d ON d.Id = f.DepartmentId
WHERE f.Rank <= 3;