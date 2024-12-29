# Database

## How would you secure a MongoDB database?

**Authentication and Authorisation**

- Use RBAC to ensure users and applications only have the minimum level of access needed to perform their jobs.
- Enforce strong passwords and use authentication mechanisms

**Encryption**

- Use TLS/SSL to encrypt data in transit.
- Enable encryption at rest using built-in encryption features

**Network Security**

- Only access the database on trusted netowrks, restrict access using firewalls by binding it to specific IP address.
- Disable remote access to the database unless necessary, and use VPNs for remote access

**Auditing**

Enable auditing to track access to sensitive data and actions taken by users.

## Our DB was stolen/exfiltrated. It was secured with one round of SHA-256 with a static salt

- SHA-256 with static salt is not sufficient for securely storing sensitive data
- SHA-256 is a cryptographic hash function, but it is not designed for securely hashing passwords because:
  - It is too fast, meaning attackers can quickly brute-force or try many passwords (especially with modern hardware).
  - Static salts don’t provide enough uniqueness or randomness across hashes, making them vulnerable to rainbow table attacks.

**Actions**

- Revoke/reset user credentials by forcing a password reset for all users whose passwords were stored in the database.
- Use stronger hashing algorithms design for password storage such as `bcrypt, Argon2`. These algorithms are slow by design and require significant computational effort to hash passwords, making brute force attacks impractical.
- Instead of using a static salt, it’s better to use a unique, random salt for each password or piece of data. This ensures that even if two users have the same password, their hashes will be different because of the unique salts.
- Monitor for suspicious activity, look for signs of unauthorised access to systems using these compromised credentials.

## 6 Aggregate functions of SQL

SQL provides several aggregate functions that perform calculations on sets of data. The 6 common aggregate functions are:

1. COUNT():
   - Usage: Returns the number of rows that match a specified condition.
   - Example: SELECT COUNT(\*) FROM employees WHERE department = 'HR';
2. SUM():
   - Usage: Returns the sum of a numeric column.
   - Example: SELECT SUM(salary) FROM employees WHERE department = 'HR';
3. AVG():
   - Usage: Returns the average value of a numeric column.
   - Example: SELECT AVG(salary) FROM employees WHERE department = 'HR';
4. MIN():
   - Usage: Returns the minimum value in a column.
   - Example: SELECT MIN(salary) FROM employees WHERE department = 'HR';
5. MAX():
   - Usage: Returns the maximum value in a column.
   - Example: SELECT MAX(salary) FROM employees WHERE department = 'HR';
6. GROUP_CONCAT() (in MySQL) / STRING_AGG() (in PostgreSQL):
   - Usage: Returns a concatenated string of values from a group.
   - Example: SELECT GROUP_CONCAT(employee_name) FROM employees WHERE department = 'HR';
