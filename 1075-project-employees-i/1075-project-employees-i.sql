# Write your MySQL query statement below
SELECT p.project_id, ROUND(AVG(experience_years),2) AS average_years
FROM Employee e
Left Join Project p
ON p.employee_id=e.employee_id
GROUP BY p.project_id
HAVING p.project_id is NOT NULL;