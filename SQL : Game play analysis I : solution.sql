-- Promblem - Game play analysis 
-- Leetcode and diffculty level - 511 & easy 
select player_id,min(event_date) as first_login
from Activity
group by player_id
