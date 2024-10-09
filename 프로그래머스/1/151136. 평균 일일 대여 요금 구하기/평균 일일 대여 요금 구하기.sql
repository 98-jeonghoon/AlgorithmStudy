-- 코드를 입력하세요
SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
from car_rental_company_car 
where car_type = "SUV";