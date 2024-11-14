-- Exploratory Data Analysis

select *
from layoffs_staging2;

select max(total_laid_off), max(percentage_laid_off)
from layoffs_staging2;

select *
from layoffs_staging2
where percentage_laid_off = 1
order by total_laid_off desc;


-- how many total layoffs per company?

select company, sum(total_laid_off)
from layoffs_staging2
group by company
order by 2 desc;


-- how many layoffs total and in what timeframe?

select min(`date`), max(`date`), sum(total_laid_off)
from layoffs_staging2;


-- which industry had the largest loss?

select industry, sum(total_laid_off)
from layoffs_staging2
group by industry
order by 2 desc;

-- country?

select country, sum(total_laid_off)
from layoffs_staging2
group by country
order by 2 desc;

-- which year had the most lay offs?

select year(`date`), sum(total_laid_off)
from layoffs_staging2
group by year (`date`)
order by 1 desc;

-- at which stage of the company?

select stage, sum(total_laid_off)
from layoffs_staging2
group by stage
order by 2 desc;


-- layoffs per month:

select substring(`date`, 1, 7) as `month`, sum(total_laid_off)
from layoffs_staging2
where substring(`date`, 1, 7)
group by `month`
order by 1 asc
;

select *
from layoffs_staging2;


-- additive total over month:
-- first make a CTE ('working memory' table)
-- apply rolling total to it ordered by month:

with rolling_total as
(
select substring(`date`, 1, 7) as `month`, sum(total_laid_off) as tl_off
from layoffs_staging2
where substring(`date`, 1, 7)
group by `month`
order by 1 asc
)
select `month`, tl_off, sum(tl_off) over(order by `month`) as Rolling_Total
from rolling_total;

-- rolling total per year (partition by year):

WITH rolling_total AS
(
    SELECT 
        SUBSTRING(`date`, 1, 7) AS `month`, 
        SUM(total_laid_off) AS tl_off
    FROM layoffs_staging2
    GROUP BY `month`
    ORDER BY 1 ASC
)

SELECT `month`, tl_off, SUM(tl_off)
	OVER(PARTITION BY substring(`month`, 1, 4) ORDER BY `month`) AS Rolling_Total
FROM rolling_total;


-- using CTE's to group layoffs per company per year,
-- and partition by each year (2020, 2021, 2022, 2023)
-- then rank the companies that laid off the most per year:


with company_layoffs as
(
select company, year(`date`) as years, sum(total_laid_off) as tl_off
from layoffs_staging2
group by company, years
),
company_layoff_rank as
(
select *, dense_rank() over(partition by years order by tl_off desc) as ranking
from company_layoffs
where tl_off is not null
)
select *
from company_layoff_rank
where ranking <= 5;




















