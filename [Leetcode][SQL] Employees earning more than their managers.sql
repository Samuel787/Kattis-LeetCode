# Write your MySQL query statement below
Select a.Name as Employee
from Employee a
where a.Salary > (
Select b.Salary
from Employee b
where a.ManagerId = b.id
);