USE SQLPractice 
GO


-- Check if the table exists before creating it
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Views')
BEGIN
    CREATE TABLE Views (
        article_id INT,
        author_id INT,
        viewer_id INT,
        view_date DATE
    );
END;

-- Truncate the table
TRUNCATE TABLE Views;

-- Insert data into the table
INSERT INTO Views (article_id, author_id, viewer_id, view_date) 
VALUES (1, 3, 5, '2019-08-01');

INSERT INTO Views (article_id, author_id, viewer_id, view_date) 
VALUES (1, 3, 6, '2019-08-02');

INSERT INTO Views (article_id, author_id, viewer_id, view_date) 
VALUES (2, 7, 7, '2019-08-01');

INSERT INTO Views (article_id, author_id, viewer_id, view_date) 
VALUES (2, 7, 6, '2019-08-02');

INSERT INTO Views (article_id, author_id, viewer_id, view_date) 
VALUES (4, 7, 1, '2019-07-22');

INSERT INTO Views (article_id, author_id, viewer_id, view_date) 
VALUES (3, 4, 4, '2019-07-21');

-- This row appears to be a duplicate of the previous one, but it is allowed to be inserted
INSERT INTO Views (article_id, author_id, viewer_id, view_date) 
VALUES (3, 4, 4, '2019-07-21');

select * from Views


/*
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.

 

Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
*/

-- sql query below

select distinct v.author_id as id  from Views as v
where v.author_id = v.viewer_id
order by v.author_id asc
