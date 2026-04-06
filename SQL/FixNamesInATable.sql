-- Create table if it does not exist
CREATE TABLE IF NOT EXISTS Users (
    user_id INT,
    name VARCHAR(40)
);

-- Truncate the table
TRUNCATE TABLE Users;

-- Insert data into the table
INSERT INTO Users (user_id, name) VALUES (1, 'aLice');
INSERT INTO Users (user_id, name) VALUES (2, 'bOB');


SELECT user_id,
       UPPER(LEFT(name, 1)) || SUBSTRING(LOWER(name) FROM 2) AS name
FROM Users
ORDER BY user_id;

-- MySQL version
SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;