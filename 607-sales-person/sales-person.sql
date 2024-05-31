# Write your MySQL query statement below
select s.name from Orders o join company c on o.com_id = c.com_id and c.name='RED' RIGHT JOIN salesperson s on s.sales_id = o.sales_id where o.sales_id IS NULL