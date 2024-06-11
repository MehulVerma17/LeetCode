# Write your MySQL query statement below
SELECT DISTINCT P1.Email from Person P1,Person P2 where P1.id <> P2.id and P1.Email=P2.Email