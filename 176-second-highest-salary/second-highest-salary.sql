-- Write your PostgreSQL query statement below
SELECT (SELECT distinct salary  from employee order by salary desc limit 1 offset 1) as "SecondHighestSalary";