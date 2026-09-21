# Write your MySQL query statement below
select Distinct author_id AS id
FROM Views
Where author_id=viewer_id 
Order By author_id;