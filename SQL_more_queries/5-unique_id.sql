-- Write a script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(
    id int PRIMARY KEY DEFAULT 1,
    name varchar(256)
);