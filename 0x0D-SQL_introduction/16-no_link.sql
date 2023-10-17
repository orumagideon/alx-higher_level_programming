-- retrieve all records from the second_table
-- table in MySQL, ordered by score in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
