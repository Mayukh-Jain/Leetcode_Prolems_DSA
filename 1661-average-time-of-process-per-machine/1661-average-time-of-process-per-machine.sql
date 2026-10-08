# Write your MySQL query statement below
select s.machine_id , ROUND(AVG(e.timestamp-s.timestamp),3) AS processing_time
FROM Activity as s JOIN Activity as e On s.process_id=e.process_id AND s.activity_type="start" and e.activity_type="end" and s.machine_id=e.machine_id
Group By s.machine_id