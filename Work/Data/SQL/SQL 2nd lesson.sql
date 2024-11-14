-- SECOND LESSON - 'WHERE' CLAUSE
-- Nomenclature: ('<, >, =, !=, <=, >=',
-- 'WHERE', 'AND', 'OR', 'NOT', 'LIKE'
-- '%' = anything, '_' = specific value)

-- Examples:

-- outputting tables with specified values, chars or dates:
SELECT *
FROM employee_salary
WHERE first_name = 'Leslie'
;

SELECT *
FROM employee_salary
WHERE salary > 50000
;

SELECT *
FROM employee_demographics
WHERE birth_date > '1970-08-08'
;

-- using logical operators to alter output:
SELECT *
FROM employee_demographics
WHERE birth_date > '1970-08-08'
AND gender = 'Male'
-- output where date is above 70's and is also male
;

SELECT *
FROM employee_demographics
WHERE birth_date > '1970-08-08'
OR gender = 'Male'
-- output where date is either above 70's OR is male
;

SELECT *
FROM employee_demographics
WHERE first_name LIKE 'Jer%'
-- output any first_name that starts with 'Jer'
;

SELECT *
FROM employee_demographics
WHERE first_name LIKE '%a%'
-- output any first_name with the letter 'a' 
;

SELECT *
FROM employee_demographics
WHERE first_name LIKE 'a____'
-- output any first_name that starts with 'a' and has '_' number of chars after
;