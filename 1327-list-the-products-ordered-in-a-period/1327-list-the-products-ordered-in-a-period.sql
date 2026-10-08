# Write your MySQL query statement below
select p.product_name, sum(o.unit) as unit
From Products p Join orders o
on p.product_id=o.product_id
WHERE o.order_date between "2020-02-01" and "2020-02-29"
Group by p.product_id 
Having sum(o.unit)>=100;