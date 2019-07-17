SELECT SUM(amount) AS total, extract(month from payment_date) AS month
from payment 
GROUP BY MONTH
ORDER BY SUM(amount) DESC 
LIMIT 1;