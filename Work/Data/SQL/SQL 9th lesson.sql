-- NINTH LESSON - 'WINDOW FUNCTIONS'

select gender, avg(salary)
from employee_demographics as dem
join employee_salary as sal
	on dem.employee_id = sal.employee_id
group by gender;


select dem.first_name, salary, gender,
avg(salary) over(partition by gender) as avg_salary
from employee_demographics as dem
join employee_salary as sal
	on dem.employee_id = sal.employee_id;
    
-- 'partition by' selects distinct values of a coloumn and applies them to the selected coloumn,
-- using the over() clause

select dem.first_name, salary, gender,
sum(salary) over(partition by gender order by dem.employee_id) as rolling_total
from employee_demographics as dem
join employee_salary as sal
	on dem.employee_id = sal.employee_id;
    
-- using 'order by' to sum up the salaries of previous rows, again partitioned by gender 

select dem.first_name, dem.last_name, salary,
row_number() over(partition by gender order by salary desc) as row_num,
rank() over(partition by gender order by salary desc) as rank_num,
dense_rank() over(partition by gender order by salary desc) as dense_rank_num
from employee_demographics as dem
join employee_salary as sal
	on dem.employee_id = sal.employee_id;
    
-- 'row_number()' assigns number based on position of row, 
-- in this example it is conditioned by 'over(partitioned by)' for gender, 
-- and oredered by salary from high to low
-- 'rank()' assigns a number to a row based on the 'order by' output and position
-- 'dense_rank()' does the same but neglects position