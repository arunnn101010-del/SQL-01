# promblem - duplicate emails 
# leetcode and diffculty level - 182 & easy 
SELECT email FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
