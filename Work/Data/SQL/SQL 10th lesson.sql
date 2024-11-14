-- TENTH LESSON - 'CTE' or 'COMMON TABLE EXPRESSION'

with CTE_Example as 
(
select gender,
 avg(salary) as avg_sal,
 max(salary) as max_sal,
 min(salary) as min_sal,
 count(salary) as count_sal
from employee_demographics as dem
join employee_salary as sal
	on dem.employee_id = sal.employee_id
group by gender
)

select *
from CTE_Example;

-- 'with' statement defines a table followed by an alias

with CTE_Example as 
(
select employee_id, gender, birth_date
from employee_demographics as dem
where birth_date > '1985-01-01'
),
CTE_Example2 as
(
select employee_id, salary
from employee_salary
where salary > 50000
)
select *
from CTE_Example as ex1
join CTE_Example2 as ex2
	on ex1.employee_id = ex2.employee_id
;
