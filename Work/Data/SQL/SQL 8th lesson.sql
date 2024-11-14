-- EIGHTH LESSON - 'CASE STATEMENTS'

select *
from employee_demographics;

select *
from employee_salary
where dept_id = 1;

-- but what if we want to use the demographcis table,
-- to show only employees from parks and recreation? 

select *
from employee_demographics
where employee_id in (select employee_id from employee_salary
where dept_id = 1);

-- matches employee id's in demographics with employee id's from salary,
-- where their dept id is equal to 1

select first_name, salary,
(select avg(salary) from employee_salary)
from employee_salary;


-- show the average salary next to the names and salaries from salary table


select gender, avg(age), max(age), min(age), count(age)
from employee_demographics
group by gender;

-- what if we want to create a table we then can manipualte like existing tables?

select gender, avg(`max(age)`), avg(`min(age)`)
from (select gender, avg(age), max(age), min(age), count(age)
from employee_demographics
group by gender)as cock
group by gender;

