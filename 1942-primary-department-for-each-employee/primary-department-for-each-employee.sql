-- Write your PostgreSQL query statement below
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'

UNION

SELECT e.employee_id, e.department_id
FROM Employee e
JOIN (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(*) = 1
) t
ON e.employee_id = t.employee_id;