
-- Create table Project if it doesn't already exist
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Project' AND xtype='U')
CREATE TABLE Project (
    project_id INT,
    employee_id INT
);

-- Create table Employee if it doesn't already exist
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Employee' AND xtype='U')
CREATE TABLE Employee (
    employee_id INT,
    name VARCHAR(10),
    experience_years INT
);

-- Truncate table Project
TRUNCATE TABLE Project;

-- Insert values into Project table
INSERT INTO Project (project_id, employee_id) VALUES (1, 1);
INSERT INTO Project (project_id, employee_id) VALUES (1, 2);
INSERT INTO Project (project_id, employee_id) VALUES (1, 3);
INSERT INTO Project (project_id, employee_id) VALUES (2, 1);
INSERT INTO Project (project_id, employee_id) VALUES (2, 4);

-- Truncate table Employee
TRUNCATE TABLE Employee;

-- Insert values into Employee table
INSERT INTO Employee (employee_id, name, experience_years) VALUES (1, 'Khaled', 3);
INSERT INTO Employee (employee_id, name, experience_years) VALUES (2, 'Ali', 2);
INSERT INTO Employee (employee_id, name, experience_years) VALUES (3, 'John', 1);
INSERT INTO Employee (employee_id, name, experience_years) VALUES (4, 'Doe', 2);

/* Write your T-SQL query statement below */
SELECT pr.project_id AS project_id, ROUND(AVG(CAST(emp.experience_years AS decimal)), 2) AS average_years
FROM Project as pr
JOIN Employee as emp ON pr.employee_id = emp.employee_id
GROUP BY pr.project_id