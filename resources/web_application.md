# Information Security Interview Preparation (Web Application Security)

## What is the OWASP (Open Web Application Security Project) Top 10 and why is it important?

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

- Use parameterised queries
- Validate and sanitise inputs
- Escape special characters
- Use Object-Relational Mapping (ORM) tools

## Describe an attack you’ve learned about (e.g., Cross-Site Scripting, Cross-Site Request Forgery) and how to defend against it

Cross-Site Scripting (XSS) occurs when an attacker injects malicious scripts into webpages viewed by other users.

- Reflected XSS
- Stored XSS
- DOM XSS

Prevention

- Sanitise and escape user inputs
- Use content security policies (CSP)
- Implement httpOnly and secure flags on cookies

CSRF attack will not be required if you can do XSS - stronger.

## What are the best practices for securely storing passwords?

- Never store passwords in plaintext.
- Hash passwords using strong algorithms like bcrypt or Argon2.
- Use salts to prevent attacks like rainbow table lookups.
- Implement a password policy to enforce complexity and rotation.

## Can you explain what XSS (Cross-Site Scripting) is and how to prevent it in web applications?

- Cross-site scripting is an attack that injects malicious code into web pages.
- 3 types of XSS, reflected, stored and DOM-based XSS.
  - Reflected and stored XSS involves the server while DOM-based XSS involves only the client.
  - XSS can be prevented by validating and sanitising user inputs so that they are not treated as codes, using security headers like `Content-Security-Policy` or using httpOnly flag to prevent JavaScript from accessing the cookie.

## Explain the concept of least privilege and why it’s important in information security

The principle of least privilege means granting users and systems only the minimum level of access needed for them to complete their tasks, this minimises the risk of accidental or malicious damage to sensitive information.

## What is a Zero-Day vulnerability? Can you provide an example of how it can be exploited?

A Zero-Day vulnerability is a previously unknown security flaw that attackers can exploit before the vendor becomes aware of releases fix for it. Example: The EternalBlue exploit, which targeted a Windows SMB vulnerability, was leveraged in ransomware attacks like WannaCry.

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
