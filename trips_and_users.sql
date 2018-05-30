# Write your MySQL query statement below
select t.Request_at Day, 
round(sum(case when t.Status like 'cancelled_%' then 1 else 0 end)/count(*),2) AS 'Cancellation Rate'
from Trips t, Users u
where u.Banned = 'No' and t.Client_Id = u.Users_Id and t.Request_at between '2013-10-01' and '2013-10-03'
group by t.Request_at