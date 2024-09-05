USE SQLPractice 
GO

-- Check if the table exists before creating it
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Products')
BEGIN
    CREATE TABLE Products (
        product_id INT,
        low_fats CHAR(1),
        recyclable CHAR(1),
        CONSTRAINT CHK_LowFats CHECK (low_fats IN ('Y', 'N')),
        CONSTRAINT CHK_Recyclable CHECK (recyclable IN ('Y', 'N'))
    );
END;

-- Truncate the table
TRUNCATE TABLE Products;

-- Insert data into the table
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (0, 'Y', 'N');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (1, 'Y', 'Y');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (2, 'N', 'Y');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (3, 'Y', 'Y');
INSERT INTO Products (product_id, low_fats, recyclable) VALUES (4, 'N', 'N');


/*
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
 

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.
*/

select distinct product_id from Products
where low_fats like '%Y%' and recyclable like '%Y%'
