-- TWELFTH LESSON - 'Stored Procedures'

select * 
from employee_salary
where salary >= 50000;


create procedure large_salaries()
select * 
from employee_salary
where salalarge_salariesry >= 50000;

call large_salaries();


delimiter $$
create procedure large_salaries2()
begin
	select *
    from employee_salary
    where salary >= 50000;
    select * 
    from employee_salary
	where salary >= 10000;
end $$
delimiter ;

call large_salaries2();


delimiter $$
create procedure large_salaries3(ID int)
begin
	select salary
    from employee_salary
    where employee_id = ID
    ;
end $$
delimiter ;

call large_salaries3(1)



























