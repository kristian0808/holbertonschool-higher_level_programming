-- 10-top_score.sql
-- Script that lists all records of the second_table ordered by score (descending)

SELECT score, name FROM second_table ORDER BY score DESC;