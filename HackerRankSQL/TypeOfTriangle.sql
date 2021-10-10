/*
Enter your query here.
*/
SELECT
    CASE
        WHEN (A = B) AND (B = C) THEN 'Equilateral'
        WHEN ((A = B) OR (A=C) OR (B=C)) AND (A + B > C) AND (A + C > B) AND (B + C > A) THEN 'Isosceles'
        WHEN (A <> B) AND (B <> c) AND (A + B > C) AND (A + C > B) AND (B + C > A) THEN 'Scalene'
        ELSE 'Not A Triangle'
    END
FROM TRIANGLES;