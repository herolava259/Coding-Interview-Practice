USE SQLPractice
GO

-- Check if the table exists before creating it
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Customer')
BEGIN
    CREATE TABLE Customer (
        id INT,
        name VARCHAR(25),
        referee_id INT
    );
END;

-- Truncate the table
TRUNCATE TABLE Customer;

-- Insert data into the table
INSERT INTO Customer (id, name, referee_id) VALUES (1, 'Will', NULL);
INSERT INTO Customer (id, name, referee_id) VALUES (2, 'Jane', NULL);
INSERT INTO Customer (id, name, referee_id) VALUES (3, 'Alex', 2);
INSERT INTO Customer (id, name, referee_id) VALUES (4, 'Bill', NULL);
INSERT INTO Customer (id, name, referee_id) VALUES (5, 'Zack', 1);
INSERT INTO Customer (id, name, referee_id) VALUES (6, 'Mark', 2);

-- sql query below 

/*
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The result format is in the following example.
*/

select c.name from dbo.Customer as c 
where c.referee_id != 2 or c.referee_id is null
