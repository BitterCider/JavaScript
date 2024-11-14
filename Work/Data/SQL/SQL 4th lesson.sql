-- 4TH Lesson - 'HAVING' and 'WHERE'
-- Examples:

SELECT gender, AVG(age)
FROM employee_demographics
-- 'WHERE AVG(age) > 40' -- not correct use
GROUP BY gender
HAVING avg(age) > 40
;

-- when selecting 'gender' and then AVG of age,
-- 'GROUP BY' occurs after trying to filter out with 'WHERE',
-- which is impossible since those rows are not rolled up yet into AVG values

SELECT occupation, AVG(salary)
FROM employee_salary
WHERE occupation LIKE '%manager%'
GROUP BY occupation
HAVING AVG(salary) > 75000
;

-- selects 'occupation' column and avg of 'salary' for each row in 'occupation'
-- filters out occupations with 'manager' in them and groups together the same occupations
-- finally filter out based on avg salary value