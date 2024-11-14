-- Data Cleaning

select * 
from layoffs;


-- 1. remove duplicates
-- 2. standardize data
-- 3. null values or blank
-- 4. remove any columns or rows



-- 1. remove duplicates

create table layoffs_staging
like layoffs;

insert layoffs_staging
select*
from layoffs;


with duplicates_cte as
(
select *,
row_number() over(
partition by company, location, industry, total_laid_off, percentage_laid_off, `date`,
 stage, country, funds_raised_millions
) as row_num 
from layoffs_staging
)
select * from duplicates_cte
where row_num > 1;


CREATE TABLE `layoffs_staging2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


select *
from layoffs_staging2;

insert into layoffs_staging2
select *,
row_number() over(
partition by company, location, industry, total_laid_off, percentage_laid_off, `date`,
 stage, country, funds_raised_millions
) as row_num 
from layoffs_staging;

delete
from layoffs_staging2
where row_num > 1;



-- 2. standardizing data

select company
from layoffs_staging2;

update layoffs_staging2
set company = trim(company);

update layoffs_staging2
set industry = 'Crypto' 
where industry like 'Crypto%';

select distinct industry
from layoffs_staging2
order by 1;

update layoffs_staging2
set country = trim(trailing '.' from country)
where country like 'United States%';

select distinct country
from layoffs_staging2
order by 1;

update layoffs_staging2
set `date` = str_to_date(`date`, '%m/%d/%Y');

alter table layoffs_staging2
modify column `date` date;


select *
from layoffs_staging2;


-- 3. null values and blanks


select * 
from layoffs_staging2
where industry is null or industry = '';

-- first see which rows in column 'industry' are 'blank'/'null' 

update layoffs_staging2
set industry = null
where industry = '';

-- set all the blank rows in 'industry' to 'null'

select t1.industry, t2.industry 
from layoffs_staging2 t1
join layoffs_staging2 t2
	on t1.company = t2.company
where t1.industry is null and t2.industry is not null;

-- see which company has multiple instances where some instances have 'null'
	-- value in 'industry'

update layoffs_staging2 t1
join layoffs_staging2 t2
	on t1.company = t2.company
set t1.industry = t2.industry
where t1.industry is null and t2.industry is not null;

-- update 'null' rows to have the same value as non 'null' of the company
-- e.g - 2 instances of Airbnb 'industry' - 'Travel' and 'Null'
-- change to 'Null' to 'Travel'

select distinct company, industry
from layoffs_staging2;


-- 4. remove any rows or columns


select *
from layoffs_staging2
where total_laid_off is null
and percentage_laid_off is null;

delete
from layoffs_staging2
where total_laid_off is null
and percentage_laid_off is null;


alter table layoffs_staging2
drop column row_num;









