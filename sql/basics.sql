-- SELECT Statement: Retrieve data from a database
SELECT column1, column2
FROM table_name;

-- WHERE Clause: Filter results based on condiitons
SELECT *
FROM employees
WHERE salary > 50000;

-- INSERT INTO: Insert data into a table
INSERT INTO employees (name, salary)
VALUES ('Joshua', 60000);

-- UPDATE: Modify existing records
UPDATE employees
SET salary = 65000
WHERE name = 'Joshua';

-- DELETE: Remove records
DELETE FROM employees
WHERE name = 'Joshua';

-- JOIN: Combine data from 2 or more tables based on a related column
-- JOIN by default is an inner join, only row that matches will be returned
SELECT employees.name, departments.dept_name
FROM employees
JOIN departments ON employees.dept_id = departments.id;

-- LEFT JOIN: Returns all records from the left table (employees), and the matched records from the right table (departments); if no match, NULL values are returned for columns from the right table
SELECT employees.name, departments.dept_name
FROM employees
LEFT JOIN departments ON employees.dept_id = departments.id;

-- RIGHT JOIN: Returns all records from the right table (departments), and the matched records from the left table (employees); if no match, NULL values are returned for columns from the left table
SELECT employees.name, departments.dept_name
FROM employees
RIGHT JOIN departments ON employees.dept_id = departments.id;

-- FULL OUTER JOIN: Returns all records when there is match in either left (employees) or right (departments) table; records without a match will have NULL values for the missing side
SELECT employees.name, departments.dept_name
FROM employees
FULL OUTER JOIN departments ON employees.dept_id = departments.id;

-- Aggregate Functions: COUNT(), SUM(), AVG(), MAX(), MIN()
SELECT COUNT(*)
FROM employees;

-- GROUP BY: Used to group results based on one or more columns
SELECT department, COUNT(*)
FROM employees
GROUP BY department;

-- HAVING: Filters the results after GROUP BY
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

-- ORDER BY: Sorts the result
SELECT *
FROM employees
ORDER BY salary DESC;
