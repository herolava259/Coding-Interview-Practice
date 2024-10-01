USE SQLPractice
GO


-- Create Employee table if it does not exist
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Employee')
BEGIN
    CREATE TABLE Employee (
        empId INT,
        name VARCHAR(255),
        supervisor INT,
        salary INT
    );
END;

-- Create Bonus table if it does not exist
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Bonus')
BEGIN
    CREATE TABLE Bonus (
        empId INT,
        bonus INT
    );
END;

-- Truncate the Employee table
TRUNCATE TABLE Employee;

-- Insert data into Employee table
INSERT INTO Employee (empId, name, supervisor, salary) 
VALUES (3, 'Brad', NULL, 4000);

INSERT INTO Employee (empId, name, supervisor, salary) 
VALUES (1, 'John', 3, 1000);

INSERT INTO Employee (empId, name, supervisor, salary) 
VALUES (2, 'Dan', 3, 2000);

INSERT INTO Employee (empId, name, supervisor, salary) 
VALUES (4, 'Thomas', 3, 4000);

-- Truncate the Bonus table
TRUNCATE TABLE Bonus;

-- Insert data into Bonus table
INSERT INTO Bonus (empId, bonus) 
VALUES (2, 500);

INSERT INTO Bonus (empId, bonus) 
VALUES (4, 2000);


/*
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.
 

Table: Bonus

+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.
 

Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
Output: 
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+
*/

select e.name as name, b.bonus as bonus from Employee as e
left join Bonus as b 
on e.empId = b.empId
where b.bonus is null or b.bonus < 1000
