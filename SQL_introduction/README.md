# SQL - Introduction

## Concepts
This project covered the following key concepts:
- What is a database and a relational database
- What SQL stands for and its purpose
- Introduction to MySQL database system
- Creating and altering databases and tables
- Inserting, selecting, updating and deleting data
- Basic SQL statements: DDL and DML
- Subqueries and functions in SQL

## Learning Objectives

- Explain what a database and a relational database are
- Describe what SQL is and what it's used for
- Create a new database in MySQL
- Define DDL and DML and give examples
- Create and modify database tables
- Insert, retrieve, update and delete data in tables
- Write basic SQL queries with subqueries
- Use built-in MySQL functions in queries

## Requirements

- Text editor (e.g. vim, emacs)
- MySQL 8.0 installed locally or access to a MySQL server

All SQL keywords should be uppercase and files should have a `.sql` extension with SQL statements commented.

## Usage

1. Install MySQL 8.0 if not installed already.
2. Connect to your MySQL server with root access.
3. Create a new database or use an existing one.
4. Create tables and insert sample data following the examples.
5. Practice writing various SQL queries based on the lesson content.

Example:

```sql
-- Create a new table
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE
);

-- Insert data
INSERT INTO users (name, email) VALUES
  ('John Doe', 'john@email.com'),
  ('Jane Smith', 'jane@email.com');
  
-- Select data
SELECT name, email FROM users;
```
Refer to the project files for the specific SQL queries I wrote to complete each task.