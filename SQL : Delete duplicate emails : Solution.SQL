-- Promblem - Delete duplicate emails 
-- Leetcode and diffculty level - 196 & easy 
delete p1 from person p1,person p2 
where p1.email=p2.email and p1.id>p2.id;

