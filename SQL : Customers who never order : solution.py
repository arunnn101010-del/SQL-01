# Promblem - Customers who never order
# Leetcode and diffculty level - 183 & easy
SELECT name as Customers
from Customers
where id not in (
    select customerId
    from Orders
);
