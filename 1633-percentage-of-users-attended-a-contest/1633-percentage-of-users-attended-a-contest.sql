# Write your MySQL query statement below
SELECT contest_id, ROUND(COUNT(u.user_id)*100/(SELECT COUNT(*) FROM Users),2) as percentage
FROM Register r
JOIN Users u
ON r.user_id=u.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;