-- fifth lesson - 'joins'

select *
from employee_demographics;

select *
from employee_salary;

select *
from employee_demographics as dem
join employee_salary as sal
	on dem.employee_id = sal.employee_id;
    
-- 'inner join' or 'join' matches rows from both columns of both tables,
-- and joins them together from left to right

select *
from employee_demographics as dem
left join employee_salary as sal
	on dem.employee_id = sal.employee_id;
    
-- 'left join' takes the selected columns from left table (dem),
-- and joins matches rows from said columns of the right table

select *
from employee_demographics as dem
right join employee_salary as sal
	on dem.employee_id = sal.employee_id;

-- 'right join' does the same but the other way around,
-- it matches the rows from the right table to the rows of the left table

select emp1.employee_id, 
emp1.first_name as santa,
emp2.employee_id,
emp2.first_name as emp
from employee_salary as emp1
join employee_salary as emp2
	on emp1.employee_id + 1 = emp2.employee_id;

-- 'self join' works the same, only difference is specifying which table we refer to,
-- ('emp1', 'emp2') as we're trying to join the same table to itself
   
select *
from employee_demographics as dem
join employee_salary as sal
	on dem.employee_id = sal.employee_id
join parks_departments as dp
	on dp.department_id = sal.dept_id;
    
 -- joining multiple tables (3 or more) together works the same   
    
    
select *
from parks_departments;
