-- SEVENTH LESSON - 'STRING FUNCTIONS'

select length('cockfall');

select first_name, length(first_name)
from employee_demographics
order by 2;

-- length() function outputs length of a string, first_name in this case

select first_name, upper(first_name)
from employee_demographics;

-- upper() outputs uppercase of selected string

select trim('              cock          ');
select ltrim('             cock          ');
select rtrim('             cock          ');

-- trims white spaces

select first_name,
left(first_name, 4),
substring(first_name, 3, 2),
birth_date,
substring(birth_date, 6, 2) as birth_month
from employee_demographics;

-- left(str, int) selects first 'int' characters from the left side of the string
-- right(str, int) same thing
-- substring(str, int, int) first 2 argument are the same, 
-- the last 'int' argument denotes how many characters are selected thereon


select first_name, replace(first_name, 's', 'z')
from employee_demographics;

-- replace() self explanatory 

select locate('c', 'cock');

select first_name, locate('An', first_name)
from employee_demographics; 

-- locate(str1, str2) returns the STARTING position of the first str within the second str

select first_name, locate('An', first_name)
from employee_demographics; 


select first_name, last_name,
concat(first_name,' ', last_name)
from employee_demographics;

-- concat(multiple str), concatinates from left argument to right


