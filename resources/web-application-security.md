# Information Security Interview Preparation (Web Application Security)

## What is OWASP (Open Web Application Security Project)?

- The OWASP Top 10 is a list of the most critical web application security risks, including issues like SQL injection, broken authentication, cross-site scripting (XSS), and more. It helps organizations identify and mitigate common vulnerabilities in web applications.
- OWASP (Open Web Application Security Project) 2024
  - Injection
  - Broken Authentication
  - Sensitive Data Exposure
  - XML External Entities
  - Broken Access Control
  - Security Misconfiguration
  - Cross-Site Scripting (XSS)
  - Insecure Deserialization
  - Using Components With Known Vulnerabilities
  - Insufficient Logging And Monitoring

## What is SQL injection, and how can it be prevented?

SQL injection is an attack where user's inputs (malicious SQL queries) are treated as commands and executed by the database.

Prevention

- Use parameterized queries
- Validate and sanitize inputs
- Escape special characters
- Use Object-Relational Mapping (ORM) tools

## Describe an attack you’ve learned about (e.g., Cross-Site Scripting, Cross-Site Request Forgery) and how to defend against it

Cross-Site Scripting (XSS) occurs when an attacker injects malicious scripts into webpages viewed by other users.

- Reflected XSS
- Stored XSS
- DOM XSS

Prevention

- Sanitize and escape user inputs
- Use content security policies (CSP)
- Implement httpOnly and secure flags on cookies

CSRF attack will not be required if you can do XSS - stronger.

## Describe a situation where you detected a security vulnerability and how you addressed it

During a vulnerability assessment of a web application, I discovered that the site was vulnerable to SQL injection attacks because user inputs weren’t properly sanitized. I immediately reported the issue to the development team. Together, we implemented input validation and used prepared statements in SQL queries to prevent injection attacks. Additionally, we ran further tests and updated the codebase to ensure the issue didn’t recur.

- Key actions:
  - Detection: Identifying the vulnerability through automated scans or manual testing.
  - Mitigation: Collaborating with the team to implement a solution (in this case, sanitizing inputs and using secure coding practices).
  - Follow-up: Verifying that the vulnerability was effectively addressed and adding further layers of security.

## What are the best practices for securely storing passwords?

- Never store passwords in plaintext.
- Hash passwords using strong algorithms like bcrypt or Argon2.
- Use salts to prevent attacks like rainbow table lookups.
- Implement a password policy to enforce complexity and rotation.

## Can you explain what XSS (Cross-Site Scripting) is and how to prevent it in web applications?

- Cross-site scripting is an attack that injects malicious code into web pages.
- 3 types of XSS, reflected, stored and DOM-based XSS.
  - Reflected and stored XSS involves the server while DOM-based XSS involves only the client.
  - XSS can be prevented by validating and sanitizing user inputs so that they are not treated as codes, using security headers like `Content-Security-Policy` or using httpOnly flag to prevent JavaScript from accessing the cookie.

## What is a Zero-Day vulnerability? Can you provide an example of how it can be exploited?

A Zero-Day vulnerability is a previously unknown security flaw that attackers can exploit before the vendor becomes aware of releases fix for it. Example: The EternalBlue exploit, which targeted a Windows SMB vulnerability, was leveraged in ransomware attacks like WannaCry.

## Zero Trust Security

Assumes no one, whether inside or outside the organization should be trusted by default. Never trust, and always verify. Cyber attacks can happen from both internal/external, every request to the system should be verified.

## CSRF Attacks

- Forged requests on behalf of a logged-in user
- Use CSRF tokens, SameSite cookies

## Security Tools

- Static Application Security Testing (SAST)
  - SonarQube
- Dynamic Application Security Test (DAST)
  - OWASP Zap
  - Burp Suite

## Policy

Same Site Origin Policy
CORS

## Secure Coding Practices

Write software in a way that protects against security vulnerabilities and ensures CIA is fulfilled.

1. Input validation
   - Valid all inputs on server side
   - Only allow digits for phone number, not text
   - Use regular expressions to validate inputs
   - Treat all user inputs as untrusted and sanitize them
2. Output encoding
   - Data displayed to user is not executed as code, to prevent XSS
     - Convert special characters `> < & "` to HTML entities (`&lt, &gt`)
     - URL encoding
     - JavaScript and CSS encoding
3. Use parameterized queries for database access to prevent SQL injections
   - No concatenation to form SQL queries
   - Parameterized queries ensure that user input is treated as data, and not executable code
4. Authentication (Prove who you are) and Authorization (Access control)
   - Hash password using strong algorithms like bcrypt
   - Add salt to prevent 2 same passwords from having the same digest, and to prevent rainbow table attacks
   - Implement MFA to add extra layer of security
   - Implement RBAC to ensure users only have access to the resources they need
   - Ensure that authentication tokens (sessionID, JWTs) are securely stored and transmitted only via HTTPS to prevent eavesdropping
5. Secure Communication
   - To prevent man-in-the-middle attacks, and avoid exposing sensitive data -> always use HTTPS (SSL/TLS) to encrypt data that is transmitted over the network
   - Use latest secure version of TLS
6. Use Strong Cryptography
   - Weak cryptography can allow attackers to easily decrypt sensitive information/tamper with it
   - Use modern cryptographic algorithms (AES-256, RSA-2048)
   - Use salt for hashing passwords and keys
   - Never hard-code sensitive keys or cryptographic secrets in the source code
   - For symmetric encryption use secure key management system to protect the keys
7. Security Headers
   - Set Content-Security-Policy (CSP) headers to control which resources can be loaded on the site
