{{ config(materialized='view') }}

WITH CustomerInfo AS (
    SELECT customerNumber AS c_id, customerName 
    FROM fil_DB1.fil_schema.customers
),
OrderInfo AS (
    SELECT orderNumber AS o_id, customerNumber, status 
    FROM fil_DB1.fil_schema.orders
),
ProductInfo AS (
    SELECT productCode, productName, buyPrice 
    FROM fil_DB1.fil_schema.products
),
OrderDetail AS (
    SELECT orderNumber, productCode, quantityOrdered, priceEach 
    FROM fil_DB1.fil_schema.orderdetails
)

SELECT 
    ci.c_id AS CustomerID,
    ci.customerName AS CustomerName,
    oi.o_id AS OrderNumber,
    pi.productName AS ProductName,
    od.quantityOrdered AS Quantity,
    od.priceEach AS PricePerItem,
    (od.quantityOrdered * od.priceEach) AS TotalPrice, 
    oi.status AS OrderStatus
FROM CustomerInfo ci
JOIN OrderInfo oi ON ci.c_id = oi.customerNumber
JOIN OrderDetail od ON oi.o_id = od.orderNumber
JOIN ProductInfo pi ON od.productCode = pi.productCode
ORDER BY ci.customerName, oi.o_id


