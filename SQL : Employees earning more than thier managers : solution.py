# Promblem - Employees earning more than thier manager
# leetcode and diffculty level - 181 & easy 
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;
