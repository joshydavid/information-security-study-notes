-- SQL Injection
SELECT * FROM users WHERE username = '' OR '1'='1' -- AND password = '';

-- Database Permission: Always restrict the access permissions of database users to the minimum required for them to perform their job (Principle of Least Privilege)
-- GRANT: Assign privileges to users
-- REVOKE: Remove privileges from users
-- SHOW GRANTS: View privileges from users
GRANT SELECT, INSERT ON database_name.* TO 'user'@'host';
REVOKE DELETE ON database_name.* FROM 'user'@'host';

-- Role-based Access Control (RBAC): Assigning roles to users to control their permissions
CREATE ROLE read_only;
GRANT SELECT ON database_name.* TO read_only;

-- Data Encryption
INSERT into employees (name, salary)
VALUES ('Joshua', AES_ENCRYPT('60000', 'encryption_key_here'));
