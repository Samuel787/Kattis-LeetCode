/*
Enter your query here.
*/
SET @number = 21;
SELECT REPEAT('* ', @number := @number -1)
FROM INFORMATION_SCHEMA.TABLES
LIMIT 20;

