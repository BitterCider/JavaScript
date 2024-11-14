-- MySQL BEGINNERS SERIES

-- FIRST LESSON - SELECT STATMENT
-- Nomenclature: ('SELECT', 'FROM', '*' = Everything, 'DISTICNT')

-- Examples:

-- outputting everything from table:
SELECT *
FROM parks_and_recreation.employee_demographics;


-- outputting coloumn(s) from table:
SELECT
first_name,
birth_date,
age
FROM parks_and_recreation.employee_demographics;

-- outputting additional column(s):
SELECT
first_name,
birth_date,
age,
age + 10
FROM employee_demographics;

-- aggregating unique values:
SELECT DISTINCT gender
FROM employee_demographics;
-- (ignores if a column contatins only unique values):
SELECT DISTINCT first_name, gender
FROM employee_demographics;






