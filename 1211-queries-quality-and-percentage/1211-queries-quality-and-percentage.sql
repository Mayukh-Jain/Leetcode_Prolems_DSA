# Write your MySQL query statement below
SELECT query_name, ROUND(SUM(rating/position)/COUNT(query_name),2) AS quality, ROUND(AVG(IF(rating<3,1,0)*100),2) as poor_query_percentage
FROM Queries
GROUP BY query_name;