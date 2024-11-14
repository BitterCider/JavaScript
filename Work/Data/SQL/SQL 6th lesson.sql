-- SIXTH LESSON - 'UNIONS'

select first_name, last_name
from employee_demographics
union 
select first_name, last_name
from employee_salary;

-- unlike join, union allows you to combine 2 or more selected columns,
-- into a single dataset
-- by default, union is 'distinct' which removes duplicates

select first_name, last_name
from employee_demographics
union all
select first_name, last_name
from employee_salary;


select first_name, last_name, 'Old' as label
from employee_demographics
where age > 50
union
-- SIXTH LESSON - 'UNIONS'

select first_name, last_name
from employee_demographics
union 
select first_name, last_name
from employee_salary;

-- unlike join, union allows you to combine 2 or more selected columns,
-- into a single dataset
-- by default, union is 'distinct' which removes duplicates

select first_name, last_name
from employee_demographics
union all
select first_name, last_name
from employee_salary;


select first_name, last_name, 'Old' as label
from employee_demographics
where age > 40
union
-- SIXTH LESSON - 'UNIONS'

select first_name, last_name
from employee_demographics
union 
select first_name, last_name
from employee_salary;

-- unlike join, union allows you to combine 2 or more selected columns,
-- into a single dataset
-- by default, union is 'distinct' which removes duplicates

select first_name, last_name
from employee_demographics
union all
select first_name, last_name
from employee_salary;


select first_name, last_name, 'Old' as label
from employee_demographics
where age > 50
union
-- SIXTH LESSON - 'UNIONS'

select first_name, last_name
from employee_demographics
union 
select first_name, last_name
from employee_salary;

-- unlike join, union allows you to combine 2 or more selected columns,
-- into a single dataset
-- by default, union is 'distinct' which removes duplicates

select first_name, last_name
from employee_demographics
union all
select first_name, last_name
from employee_salary;


select first_name, last_name, 'Old man' as label
from employee_demographics
where age > 40 and gender = 'Male'
union
select first_name, last_name, 'Old lady' as label
from employee_demographics
where age > 40 and gender = 'Female'
union
select first_name, last_name, 'highly paid' as label
from employee_salary
where salary > 70000
order by first_name, last_name;


