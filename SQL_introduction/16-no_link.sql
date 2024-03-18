-- 16-no_link.sql
-- Script that lists all records of second_table with non-null name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;