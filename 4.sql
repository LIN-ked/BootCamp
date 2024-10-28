SELECT COUNT(DISTINCT Order_id) AS Total_Orders
FROM SALES
WHERE Date='2023-03-18';

SELECT COUNT(DISTINCT s.Order_id) AS Total_Orders
FROM SALES s
JOIN CUSTOMERS c ON s.Customer_id=c.Customer_id
WHERE s.Date='2023-03-18'
AND c.First_name='John'
AND c.Last_name='Doe';

WITH January_Sales AS(
SELECT Customer_id,SUM(Revenue) AS Total_Spent
FROM SALES
WHERE Date>='2023-01-01' AND Date<'2023-02-01'
GROUP BY Customer_id
)
SELECT COUNT(DISTINCT Customer_id) AS Total_Customers,
AVG(Total_Spent) AS Avg_Spent_Per_Customer
FROM January_Sales;

SELECT i.Department,SUM(s.Revenue) AS Total_Revenue
FROM SALES s
JOIN ITEMS i ON s.Item_id=i.Item_id
WHERE s.Date>='2022-01-01' AND s.Date<'2023-01-01'
GROUP BY i.Department
HAVING SUM(s.Revenue)<600;

SELECT MAX(Revenue) AS Max_Revenue,MIN(Revenue) AS Min_Revenue
FROM SALES;

WITH Max_Revenue AS(
SELECT MAX(Revenue) AS Max_Rev FROM SALES
)
SELECT s.Order_id,i.Item_name,s.Revenue
FROM SALES s
JOIN ITEMS i ON s.Item_id=i.Item_id
WHERE s.Revenue=(SELECT Max_Rev FROM Max_Revenue);
