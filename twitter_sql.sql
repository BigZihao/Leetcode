2018(1-3月) 分析|数据科学类 硕士 全职@Twitter - 内推 - 技术电面  | Pass | 在职跳槽
table tweettweet_id, con_num, reply_to_tweet
1, 1, null  # depth:0 来源一亩.三分地论坛. 
2,1, 1 #depth 1
3,1,2 #depth 2
4,1,1 #depth 1
5,2,null #depth 0
6, 1,3# depth 3
要求output：count depth0，depth1， depth2，depth>=3
depth 0： 2
depth 1: 2. 1point 3acres 论坛
depth 2: 1
depth>=3: 1


用了三个self join做感觉不太对，我的就算抛砖引玉了，求各位大神赐教


select T3.frid as frid, T4.tweettweet_id as seid, 2 as depth  
from  
(
select T1.tweettweet_id as orid, T2.tweettweet_id as frid, 1 as depth
from Tweet T1, Tweet T2
where T1.reply_to_tweet = NULL and T1.tweettweet_id = T2.reply_to_tweet
) T3, Tweet T4
where T3.frid = T4.reply_to_tweet 

select count(distinct(con_num)) as depth_0, count(distinct(total_reply_to)) as degree_1 ,count(distinct(degree_2)),count(distinct(degree_3)). visit 1point3acres for more.
from (select *
from (select tweet3.*, tweet.tweet_id as degree_3
from (select tweet2.*,tweet.tweet_id as degree_2
from (select a.Con_num, a.tweet_id, a.reply_to_tweet,b.tweet_id as total_reply_to
from tweet a
left join tweet b
on a.tweet_id = b.reply_to_tweet
and a.con_num = b.con_num
order by a.Con_num, a.tweet_id) tweet2 
left join tweet 
on tweet2.total_reply_to = tweet.reply_to_tweet
and tweet2.con_num = tweet.con_num
order by con_num, tweet_id) tweet3
left join tweet . more info on 1point3acres
on tweet3.degree_2 = tweet.reply_to_tweet. visit 1point3acres for more.
and tweet3.con_num = tweet.con_num. 1point3acres
order by con_num, tweet_id) tweet4
where reply_to_tweet is null) tweet5

select 0 as depth, count(D0.id) from 
(select tweet_id id
from tweet 
where reply_to_tweet is null ) D0
UNION ALL
SELECT 1 AS depth, count(D1.id) AS count FROM
(select tweet_id id
from tweet 
where reply_to_tweet IN (SELECT id FROM D0)) D1, 


(
  SELECT tweet_id id
  FROM tweet
  WHERE reply_to_tweet IN (SELECT id FROM D1)
) D2, (
  SELECT tweet_id id
  FROM tweet
  WHERE tweet_id NOT IN (
    SELECT id FROM D0
    UNION ALL
    SELECT id FROM D1
    UNION ALL
    SELECT id FROM D2
  )
) D3

-- 无递归版本
WITH depth0(id, num) AS (
  SELECT tweet_id, con_num
  FROM tweet
  WHERE reply_to_tweet IS NULL
),
depth1(id, num) AS (
  SELECT tweet_id, con_num
  FROM tweet
  WHERE reply_to_tweet IN (SELECT id FROM depth0)
),
depth2(id, num) AS (
  SELECT tweet_id, con_num
  FROM tweet
  WHERE reply_to_tweet IN (SELECT id FROM depth1)
),
depth3(id, num) AS (
  SELECT tweet_id, con_num
  FROM tweet
  WHERE tweet_id NOT IN (
    SELECT id FROM depth0
    UNION ALL
    SELECT id FROM depth1
    UNION ALL
    SELECT id FROM depth2
  )
)
SELECT 0 AS depth, SUM(num) AS count FROM depth0
UNION ALL
SELECT 1 AS depth, SUM(num) AS count FROM depth1
UNION ALL
SELECT 2 AS depth, SUM(num) AS count FROM depth2
UNION ALL
SELECT 3 AS depth, SUM(num) AS count FROM depth3;










http://sqlfiddle.com/#!17/9e13b


有人愿意post一下这两道题的SQL codes？ 方便交流学习。从面经里总结的，也有自己的面经，先谢谢大家。本人SQL有点弱，得向各位大神学习。
1 sql
Table 1: Campaigns
Account_id (AID) | Campaign_id (CID)
1     123
1    234
2    235

Table 2:  Spend
Campaign_id (CID) | Date | Spend_amount | Currency
123  2017-08-01 200 USD
123 2017-08-02 150 USD
234 2017-09-01 500 USD
235 2017-07-01 100 CAD
. 留学申请论坛-一亩三分地


Table 3: Exchange_rate
Currency | Rate(to USD)
CAD  0.79
USD 1.00

q1: CID, total spend in USD

q2: AID, number of days from first spend date to highest spend date

--Q1
select CID, sum(Spend_amount*Rate)
from Spend S, Exchange_rate E,
where S.Currency = E.Currency
group by CID

--Q2
summary table 
SELECT S.c_id,  S.s_date , S.s_amount * E.e_rate as s_amount 
FROM Spend S, ExchangeRate E 
where S.s_currency = E.e_currency;



select maxSpendDate.a_id, datediff(maxDate, firstDate) as days
from

(select M1.a_id, S2.s_date as maxDate
from 
(select C.a_id, max(S.s_amount) maxSpend 
from summary S, Campaigns C
where S.c_id = C.c_id
group by a_id) M1, summary S2, Campaigns C2
where S2.c_id = C2.c_id and C2.a_id = M1.a_id and S2.s_amount = M1.maxSpend)
maxSpendDate, 

(select C.a_id, min(S.s_date) as firstDate
from Spend S, Campaigns C
where S.c_id = C.c_id
group by a_id) 
firstSpendDate

where maxSpendDate.a_id = firstSpendDate.a_id











-- Q1: CID, total spend in USD
SELECT c_id, SUM(s_amount * e_rate)
FROM Spend JOIN ExchangeRate ON s_currency = e_currency
GROUP BY c_id;










-- Q2: AID, number of days from first spend date to highest spend date
WITH SummaryTable AS (
  SELECT a_id, s_date, SUM(s_amount * e_rate) AS t_amount
  FROM Campaigns C JOIN Spend S ON C.c_id = S.c_id
                   JOIN ExchangeRate ON s_currency = e_currency
  GROUP BY a_id, s_date
), FirstSpend AS (
  SELECT a_id, s_date
  FROM (
    SELECT a_id, s_date,
           ROW_NUMBER() OVER(PARTITION BY a_id ORDER BY s_date) AS rk
    FROM SummaryTable
  ) T
  WHERE rk = 1
), HighestSpend AS (
  SELECT a_id, s_date
  FROM (
    SELECT a_id, s_date,
           ROW_NUMBER() OVER(PARTITION BY a_id ORDER BY t_amount DESC) AS rk
    FROM SummaryTable
  ) T
  WHERE rk = 1
)
SELECT F.a_id, H.s_date - F.s_date AS days
FROM FirstSpend F JOIN HighestSpend H ON F.a_id = H.a_id;
           
