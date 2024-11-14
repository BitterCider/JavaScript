-- THIRD LESSON - 'GROUP BY' and 'ORDER BY'
-- Nomenclature ['GROUP BY', 'ORDER BY', 'MAX()', 'MIN()', 'COUNT()', 'ASC', 'DESC']
-- Examples:

SELECT gender
FROM employee_demographics
GROUP BY gender;

-- GROUP BY groups together rows with the same value from selected column(s)

SELECT gender, AVG(age)
FROM employee_demographics
GROUP BY gender;

-- select the gender and average out the age column for each gender

SELECT gender, AVG(age), MAX(age) old, MIN(age) young, COUNT(age) count
FROM employee_demographics
GROUP BY gender;

-- also outputs maximum and minimum age of both male and female, as well as their count

SELECT *
FROM employee_demographics
ORDER BY gender, age;

SELECT *
FROM employee_demographics
ORDER BY age, gender;

-- sorts by ascending order, both A-Z and numerical values
-- first sort by gender and then sort by age - the order is from left to right


