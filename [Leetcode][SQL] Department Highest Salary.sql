# Write your MySQL query statement below

SELECT Department.Name AS Department, Employee.Name AS Employee, Employee.Salary AS Salary
FROM Employee JOIN Department ON Employee.DepartmentId = Department.Id
WHERE (Employee.DepartmentId, Employee.Salary) in
(SELECT DepartmentId, MAX(Salary)
from Employee
GROUP BY DepartmentId)