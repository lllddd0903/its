-- Задача №1
-- CREATE TABLE Electronics(
--  product_id int,
--  product_name varchar(50),
--  brand varchar(30),
--  price int,
--  stock int,
--  country varchar(30)
-- )

-- INSERT INTO Electronics (product_id, product_name, brand, price, stock, country)
-- VALUES 
-- (1, 'Notebook', 'Macbook', 50000, 3, 'USA'),
-- (2, 'Notebook', 'Asus', 30000, 4, 'Russia'),
-- (3, 'Monitor', 'Acer', 10000, 2, 'KZ'),
-- (4, 'Monitor', 'Xiaomi', 8000, 3, 'China'),
-- (5, 'Keyboard', 'Apple', 20000, 6, 'USA'),
-- (6, 'Keyboard', 'Huawei', 9000, 7, 'China'),
-- (7, 'Computer_mice', 'Acer', 2000, 3, 'KZ'),
-- (8, 'Computer_mice', 'Macbook', 5000, 5, 'USA');

-- SELECT *
-- FROM Electronics

-- SELECT *
-- FROM Electronics 
-- WHERE price > 100000

-- SELECT *
-- FROM Electronics
-- WHERE country = 'USA'
-- AND price < 50000;

-- SELECT *
-- FROM Electronics
-- WHERE brand = 'Samsung' or brand = 'Apple';

-- SELECT *
-- FROM Electronics
-- Where stock IN (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15);

-- UPDATE Electronics
-- SET price = price * 1.1
-- WHERE country = 'China';

-- UPDATE Electronics
-- SET price = 0
-- WHERE stock < 3;

-- DELETE FROM Electronics
-- WHERE price < 10000;

-- SELECT *
-- FROM Electronics;

-- Задача №2
-- CREATE TABLE Students(
--  student_id int,
--  first_name varchar(30),
--  last_name varchar(30),
--  age int,
--  gpa float,
--  major varchar(50),
--  country varchar(30)
-- )

-- INSERT INTO Students (student_id, first_name, last_name, age, gpa, major, country)
--VALUES
--(1, 'Иван', 'Петров', 20, 3.8, 'Computer Science', 'KZ'),
--(2, 'Мария', 'Сидорова', 19, 3.6, 'Business', 'USA'),
--(3, 'Петр', 'Иванов', 21, 2.9, 'Engineering', 'Germany'),
--(4, 'Анна', 'Кузнецова', 22, 3.9, 'Medicine', 'Canada'),
--(5, 'Дмитрий', 'Смирнов', 20, 3.2, 'Computer Science', 'KZ'),
--(6, 'Ольга', 'Морозова', 18, 3.4, 'Business', 'USA'),
--(7, 'Алексей', 'Волков', 23, 3.7, 'Engineering', 'Germany'),
--(8, 'Елена', 'Федорова', 21, 3.1, 'Medicine', 'Canada'),
--(9, 'Нуржан', 'Ахметов', 22, 3.5, 'Computer Science', 'KZ'),
--(10, 'Таро', 'Ямамото', 24, 3.9, 'Engineering', 'Japan');

-- SELECT *
-- From Students

--SELECT *
--From Students
--WHERE gpa > 3.5;

--SELECT *
--From Students
--WHERE major = 'Computer Science' AND age > 20;

--SELECT *
--From Students
--WHERE country = 'USA' or country = 'KZ';

--SELECT *
--From Students
--WHERE age BETWEEN 19 AND 22;

--SELECT *
--From Students
--WHERE first_name IN ('Иван', 'Мария', 'Петр');

-- UPDATE Students
-- SET gpa = gpa + 0.2
-- WHERE gpa >= 3.5;

--UPDATE Students
--SET age = 21
--WHERE student_id = 5;

--UPDATE Students
--SET major = "Data Science"
--WHERE major = 'Computer Science' AND gpa > 3.7;

--DELETE FROM Students
--WHERE gpa < 2.0;

--DELETE FROM Students
--WHERE age < 18;

--SELECT * 
--FROM Students
--WHERE gpa > 3.0

--Задача №3
--CREATE TABLE Products(
--  product_id int,
--  product_name varchar(50),
--  category varchar(30),
--  price int,
--  stock int
--)

--CREATE TABLE Orders(
--  order_id int,
--  product_id int,
--  quantity int,
--  customer_name varchar(50),
--  order_date varchar(20),
--  status varchar(20)
--)

--INSERT INTO Products (product_id, product_name, category, price, stock)
--VALUES
--(1, 'Laptop', 'Electronics', 450000, 5),
--(2, 'Smartphone', 'Electronics', 280000, 10),
--(3, 'T-Shirt', 'Clothing', 15000, 25),
--(4, 'Jeans', 'Clothing', 30000, 15),
--(5, 'Apple', 'Food', 500, 100),
--(6, 'Bread', 'Food', 400, 50),
--(7, 'Book SQL Basics', 'Books', 8000, 20),
--(8, 'Vacuum Cleaner', 'Home', 120000, 4),
--(9, 'Microwave', 'Home', 95000, 6);

--INSERT INTO Orders (order_id, product_id, quantity, customer_name, order_date, --status)
--VALUES
--(1, 1, 1, 'Alice', '2025-01-10', 'completed'),
--(2, 2, 2, 'Bob', '2025-01-11', 'pending'),
--(3, 3, 3, 'Charlie', '2025-01-12', 'completed'),
--(4, 4, 1, 'Alice', '2025-01-13', 'cancelled'),
--(5, 5, 10, 'David', '2025-01-14', 'completed'),
--(6, 6, 5, 'Bob', '2025-01-15', 'pending'),
--(7, 7, 2, 'Eva', '2025-01-16', 'completed'),
--(8, 8, 1, 'Frank', '2025-01-17', 'completed'),
--(9, 9, 1, 'Alice', '2025-01-18', 'pending'),
--(10, 2, 1, 'Charlie', '2025-01-19', 'completed')

--SELECT * 
--FROM Products

--SELECT *
--FROM Orders

--SELECT * 
--FROM Products
--WHERE price > 50000

--SELECT * 
--FROM Products
--WHERE category = 'Electronics' AND stock > 5

--SELECT * 
--FROM Orders
--WHERE status = 'completed'

--CREATE TABLE Orders_Food (
--    order_id INT,
--    product_id INT,
--    quantity INT,
--    customer_name VARCHAR(50),
--    order_date VARCHAR(20),
--    status VARCHAR(20)
--)

--INSERT INTO Orders_Food (order_id, product_id, quantity, customer_name, -order_date, status)
--VALUES
--(6, 6, 5, 'Саша', '2025-01-15', 'completed'),
--(10, 6, 2, 'Маша', '2025-01-19', 'completed'),
--(7, 7, 10, 'Катя', '2025-01-16', 'pending')

--SELECT * FROM Orders
--WHERE quantity BETWEEN 2 AND 5

--SELECT * 
--FROM Orders
--WHERE customer_name IN ('Alice', 'Bob')

--UPDATE Products
--SET price = price + 5000
--WHERE category = 'Electronics'

--UPDATE Products
--SET stock = stock - 2
--WHERE price > 100000

--UPDATE Order
--SET status = 'completed'
--WHERE status = 'pending'

--UPDATE Products
--SET stock = 0
--WHERE price > 200000

--DELETE FROM Products
--WHERE stock = 0

--DELETE FROM Orders
--WHERE status = 'cancelled'

--SELECT * FROM Products
--WHERE price BETWEEN 30000 AND 150000

--SELECT * FROM Orders
--WHERE status = 'completed'

--SELECT * FROM Products
--WHERE stock < 3


--Задача №4
--CREATE TABLE Employees(
--  employee_id int,
--  first_name varchar(30),
--  last_name varchar(30),
--  position varchar(50),
--  salary int,
--  department varchar(30),
--  hire_date varchar(20),
--  age int
--)

--INSERT INTO Employees (employee_id, first_name, last_name, position, salary, department, hire_date, age)
--VALUES
--(1, 'Иван', 'Петров', 'CEO', 5000000, 'Management', '2010-01-15', 50),
--(2, 'Мария', 'Сидорова', 'Developer', 1500000, 'IT', '2018-06-01', 28),
--(3, 'Петр', 'Иванов', 'Designer', 1200000, 'IT', '2019-03-10', 26),
--(4, 'Анна', 'Смирнова', 'Manager', 2000000, 'HR', '2015-09-20', 38),
--(5, 'Олег', 'Кузнецов', 'Accountant', 1000000, 'Finance', '2016-07-12', 33),
--(6, 'Екатерина', 'Морозова', 'Developer', 1800000, 'IT', '2020-02-05', 30),
--(7, 'Алексей', 'Соколов', 'Manager', 2200000, 'Sales', '2014-11-01', 42),
--(8, 'Светлана', 'Федорова', 'Designer', 1300000, 'IT', '2017-08-15', 27),
--(9, 'Дмитрий', 'Волков', 'Accountant', 900000, 'Finance', '2012-04-20', 36),
--(10, 'Наталья', 'Климова', 'Manager', 2500000, 'HR', '2013-05-30', 45)

--SELECT * 
--FROM Employees

--SELECT * 
--FROM Employees
--WHERE department = 'IT'

--SELECT * 
--FROM Employees
--WHERE position = 'Manager'

--SELECT * 
--FROM Employees
--WHERE salary > 2000000

--SELECT * 
--FROM Employees
--WHERE department = 'IT' AND position = 'Developer'

--SELECT * 
--FROM Employees
--WHERE age BETWEEN 25 AND 40

--SELECT * 
--FROM Employees
--WHERE department IN ('Finance', 'HR')

--SELECT * 
--FROM Employees
--WHERE salary BETWEEN 1000000 AND 3000000

--UPDATE Employees
--SET salary = salary + 200000
--WHERE position = 'Developer'

--UPDATE Employees
--SET salary = salary * 1.10
--WHERE department = 'IT'

--UPDATE Employees
--SET department = "Management"
--WHERE position = "Manager"

--UPDATE Employees
--SET salary = 300000
--WHERE age > 60

--DELETE FROM Employees
--WHERE hire_date < '2015-01-01'

--DELETE FROM Employees
--WHERE salary < 600000

--SELECT * 
--FROM Employees
--WHERE department = 'IT' AND salary > 1500000

--SELECT * 
--FROM Employees
--WHERE salary > 3000000

--SELECT * 
--FROM Employees
--WHERE age < 30