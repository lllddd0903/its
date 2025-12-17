--Задача№1
--CREATE TABLE Customers (
--    customer_id INTEGER PRIMARY KEY,
--    first_name VARCHAR(100),
--    last_name VARCHAR(100),
--    age INTEGER,
--    country VARCHAR(100)
--);

--CREATE TABLE Orders (
--  order_id INTEGER PRIMARY KEY,
--  item VARCHAR(100),
--  amount INTEGER,
--  customer_id INTEGER,
--  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
--)

--INSERT INTO Customers (customer_id, first_name, last_name, age, country)
--VALUES
--(1, 'Alice', 'Smith', 25, 'USA'),
--(2, 'Bob', 'Jones', 30, 'Canada'),
--(3, 'Charlie', 'Brown', 22, 'UK'),
--(4, 'Diana', 'Wilson', 28, 'USA'),
--(5, 'Emma', 'Davis', 35, 'Canada'),
--(6, 'Frank', 'Miller', 27, 'USA');

--INSERT INTO Orders (order_id, item, amount, customer_id)
--VALUES (1, 'Keyboard', 50000, 1),
--       (2, 'Mouse', 30000, 1),
--       (3, 'Monitor', 150000, 2),
--       (4, 'Headset', 80000, 4),
--       (5, 'Keyboard', 50000, 3),
--       (6, 'Monitor', 150000, 5),
--       (7, 'Mouse', 30000, 2),
--       (8, 'Keyboard', 50000, 6),
--       (9, 'Webcam', 60000, 4),
--       (10, 'Monitor', 150000, 1)

--SELECT c.first_name, c.last_name, o.item, o.amount
--FROM Customers as c
--JOIN Orders as o ON o.customer_id = c.customer_id;

--SELECT c.first_name, c.last_name, o.item, o.amount
--FROM Orders as o
--JOIN Customers as c ON o.customer_id = c.customer_id
--ORDER BY o.amount DESC
--LIMIT 5;

--SELECT c.first_name, c.last_name, o.item, o.amount
--FROM Orders as o
--JOIN Customers as c ON o.customer_id = c.customer_id
--WHERE c.first_name = 'Alice'

--SELECT c.first_name, c.last_name, c.country, o.item, o.amount
--FROM Orders as o
--JOIN Customers as c ON o.customer_id = c.customer_id
--WHERE c.country = 'USA'

--SELECT c.first_name, c.last_name, o.item, o.amount
--FROM Orders as o
--JOIN Customers as c ON o.customer_id = c.customer_id
--ORDER BY o.amount DESC
--LIMIT 1;


--Задача №2

--CREATE TABLE Products(
--  product_id int,
--  product_name varchar(100),
--  category varchar(50),
--  price int
--)

--INSERT INTO Products (product_id, product_name, category, price)
--VALUES (1, 'Laptop', 'Electronics', 1000000),
--       (2, 'Mouse', 'Electronics', 50000),
--       (3, 'Keyboard', 'Electronics', 100000),
--       (4, 'Monitor', 'Electronics', 300000),
--       (5, 'Shirt', 'Clothing', 30000),
--       (6, 'Jeans', 'Clothing', 60000),
--       (7, 'Shoes', 'Clothing', 80000),
--       (8, 'Apple', 'Food', 500),
--       (9, 'Banana', 'Food', 300),
--       (10, 'Orange', 'Food', 400)

--CREATE TABLE Sales(
--  sale_id int,
--  product_id int,
--  quantity int,
--  sale_date varchar(20)
--)

--INSERT INTO Sales (sale_id, product_id, quantity, sale_date)
--VALUES (1, 1, 2, '2025-01-10'),
--       (2, 2, 5, '2025-01-10'),
--       (3, 3, 3, '2025-01-11'),
--       (4, 4, 1, '2025-01-11'),
--       (5, 5, 10, '2025-01-12'),
--       (6, 6, 4, '2025-01-12'),
--       (7, 7, 2, '2025-01-13'),
--       (8, 8, 20, '2025-01-13'),
--       (9, 9, 15, '2025-01-14'),
--       (10, 10, 12, '2025-01-14'),
--       (11, 1, 1, '2025-01-15'),
--       (12, 2, 8, '2025-01-15'),
--       (13, 3, 6, '2025-01-15'),
--       (14, 4, 2, '2025-01-16'),
--       (15, 5, 5, '2025-01-16')

--SELECT p.product_name, s.quantity, p.price, s.sale_date
--FROM Sales as s
--JOIN Products as p ON p.product_id = s.product_id

--SELECT p.product_name, s.quantity, p.price
--FROM Sales as s
--JOIN Products as p ON p.product_id = s.product_id
--ORDER BY p.price DESC
--LIMIT 5;

--SELECT p.product_name, s.quantity, p.price, p.category
--FROM Sales as s
--JOIN Products as p ON p.product_id = s.product_id
--WHERE p.category = 'Electronics'

--SELECT p.product_name, s.quantity, s.sale_date
--FROM Sales as s
--JOIN Products as p ON p.product_id = s.product_id
--ORDER BY s.quantity DESC
--LIMIT 3;

--SELECT p.product_name, s.quantity, p.price, p.category
--FROM Sales as s
--JOIN Products as p ON p.product_id = s.product_id
--ORDER BY p.price ASC
--WHERE category = 'Clothing'


--Задача №3
--CREATE TABLE Teachers(
--  teacher_id int,
--  first_name varchar(100),
--  last_name varchar(100),
--  subject varchar(50),
--  salary int
--)

--CREATE TABLE Grades(
--  grade_id int,
--  student_name varchar(100),
--  teacher_id int,
--  subject varchar(50),
--  score int
--)

--INSERT INTO Teachers (teacher_id, first_name, last_name, subject, salary)
--VALUES (1, 'Alexander', 'Smirnov', 'Math', 1500000),
--       (2, 'Elena', 'Petrova', 'English', 1200000),
--       (3, 'Sergey', 'Ivanov', 'Physics', 1400000),
--       (4, 'Marina', 'Sokolova', 'Chemistry', 1300000),
--       (5, 'Dmitry', 'Lebedev', 'History', 1100000)

--INSERT INTO Grades (grade_id, student_name, teacher_id, subject, score)
--VALUES (1, 'Ivan', 1, 'Math', 85),
--       (2, 'Ivan', 2, 'English', 92),
--       (3, 'Ivan', 3, 'Physics', 78),
--       (4, 'Maria', 1, 'Math', 90),
--       (5, 'Maria', 2, 'English', 88),
--       (6, 'Maria', 3, 'Physics', 82),
--       (7, 'Petr', 1, 'Math', 95),
--       (8, 'Petr', 2, 'English', 91),
--       (9, 'Petr', 3, 'Physics', 89),
--       (10, 'Anna', 1, 'Math', 72),
--       (11, 'Anna', 2, 'English', 85),
--       (12, 'Anna', 3, 'Physics', 80),
--       (13, 'Nikolay', 4, 'Chemistry', 88),
--       (14, 'Nikolay', 5, 'History', 92),
--       (15, 'Sofia', 4, 'Chemistry', 91),
--       (16, 'Sofia', 5, 'History', 87),
--       (17, 'Dmitry', 1, 'Math', 93),
--       (18, 'Dmitry', 4, 'Chemistry', 86),
--       (19, 'Natalia', 2, 'English', 94),
--      (20, 'Natalia', 5, 'History', 89)

--SELECT g.student_name, g.subject, g.score, t.first_name, t.last_name
--FROM Grades as g
--JOIN Teachers as t ON t.teacher_id = g.teacher_id

--SELECT g.student_name, g.subject, g.score, t.first_name, t.last_name
--FROM Grades as g
--JOIN Teachers as t ON t.teacher_id = g.teacher_id
--WHERE g.score > 85
--ORDER BY g.score DESC

--SELECT g.student_name, g.subject, g.score, t.first_name, t.last_name
--FROM Grades as g
--JOIN Teachers as t ON t.teacher_id = g.teacher_id
--WHERE t.subject = 'Math'

--SELECT g.student_name, g.subject, g.score, t.first_name, t.last_name
--FROM Grades as g
--JOIN Teachers as t ON t.teacher_id = g.teacher_id
--ORDER BY g.score DESC
--LIMIT 5

--SELECT g.student_name, g.score, t.first_name, t.last_name
--FROM Grades as g
--JOIN Teachers as t ON t.teacher_id = g.teacher_id
--WHERE g.teacher_id = 1


--Задача №4
--CREATE TABLE Categories( category_id int, category_name varchar(100) )

--CREATE TABLE Products( product_id int, product_name varchar(100), category_id int, price int, stock int )

--INSERT INTO Categories (category_id, category_name)
--VALUES (1, 'Laptops'),
--       (2, 'Phones'),
--       (3, 'Tablets'),
--       (4, 'Accessories')

--INSERT INTO Products (product_id, product_name, category_id, price, stock)
--VALUES (1, 'MacBook Pro', 1, 2000000, 10),
--       (2, 'Dell XPS', 1, 1500000, 8),
--       (3, 'iPhone 14', 2, 800000, 20),
--       (4, 'Samsung S23', 2, 700000, 15),
--       (5, 'iPad Pro', 3, 600000, 12),
--       (6, 'Samsung Tab', 3, 400000, 18),
--       (7, 'USB-C Cable', 4, 15000, 100),
--       (8, 'Phone Case', 4, 30000, 80),
--       (9, 'Screen Protector', 4, 10000, 150),
--       (10, 'Charger', 4, 50000, 60)

--SELECT p.product_name, c.category_name, p.price, p.stock
--FROM Products as p
--JOIN Categories as c ON p.category_id = c.category_id

--SELECT p.product_name, c.category_name, p.price, p.stock
--FROM Products as p
--JOIN Categories as c ON p.category_id = c.category_id
--WHERE c.category_name = 'Laptops'

--SELECT p.product_name, c.category_name, p.price
--FROM Products as p
--JOIN Categories as c ON p.category_id = c.category_id
--ORDER BY p.price DESC
--LIMIT 5

--SELECT p.product_name, c.category_name, p.price, p.stock
--FROM Products as p
--JOIN Categories as c ON p.category_id = c.category_id
--WHERE c.category_name = 'Accessories'
--ORDER BY p.price DESC

--SELECT p.product_name, c.category_name, p.price, p.stock
--FROM Products as p
--JOIN Categories as c ON p.category_id = c.category_id
--WHERE p.stock > 50
--ORDER BY p.stock DESC
--LIMIT 3

-- Задача №5

--CREATE TABLE Departments( department_id int, department_name varchar(100) )

--CREATE TABLE Employees(
--  employee_id int,
--  first_name varchar(100),
--  last_name varchar(100),
--  department_id int,
--  salary int,
--  hire_date varchar(20)
--)

--INSERT INTO Departments (department_id, department_name)
--VALUES (1, 'IT'),
--       (2, 'HR'),
--       (3, 'Finance'),
--       (4, 'Sales'),
--       (5, 'Management')

--INSERT INTO Employees (employee_id, first_name, last_name, department_id, salary, hire_date)
--VALUES (1, 'Ivan', 'Petrov', 1, 2000000, '2020-01-15'),
--       (2, 'Maria', 'Sidorova', 1, 1800000, '2019-03-20'),
--       (3, 'Petr', 'Ivanov', 2, 1200000, '2021-06-10'),
--       (4, 'Anna', 'Smirnova', 3, 1500000, '2020-09-05'),
--       (5, 'Nikolay', 'Popov', 4, 1600000, '2018-11-12'),
--       (6, 'Sofia', 'Volkova', 4, 1400000, '2022-01-30'),
--       (7, 'Dmitry', 'Sokolov', 5, 2500000, '2017-05-22'),
--       (8, 'Natalia', 'Kuznetsova', 1, 1900000, '2021-02-14')

--SELECT e.first_name, e.last_name, d.department_name, e.salary
--FROM Employees as e
--JOIN Departments as d ON d.department_id = e.department_id

--SELECT e.first_name, e.last_name, d.department_name, e.salary
--FROM Employees as e
--JOIN Departments as d ON d.department_id = e.department_id
--WHERE d.department_name = 'IT'

--SELECT e.first_name, e.last_name, d.department_name, e.salary
--FROM Employees as e
--JOIN Departments as d ON d.department_id = e.department_id
--ORDER by e.salary DESC
--LIMIT 5

--SELECT e.first_name, e.last_name, d.department_name, e.salary
--FROM Employees as e
--JOIN Departments as d ON d.department_id = e.department_id
--WHERE e.salary >1500000
--ORDER BY e.salary DESC

--SELECT e.first_name, e.last_name, d.department_name, e.salary, e.hire_date
--FROM Employees as e
--JOIN Departments as d ON d.department_id = e.department_id
--WHERE d.department_name = 'IT'
--AND e.hire_date > '2020-12-31'
