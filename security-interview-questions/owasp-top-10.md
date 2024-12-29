# OWASP Top 10 (Open Web Application Security Project)

## What is SQL injection?

SQL injection is a type of attack where an attacker injects malicious SQL code into a query. This allows the attacker to manipulate the SQL query that the application uses to interact with a database, potentially granting unauthorized access to sensitive data, altering or deleting records, or even executing administrative operations on the database.

Web applications that accept user inputs (like search boxes, login forms, or any other fields) can be vulnerable if these inputs are directly inserted into SQL queries without proper validation or sanitization.

### Consequences

- Unauthorized Access: Attackers can log in without valid credentials.
- Data Exfiltration: Attackers can extract sensitive information from the database, such as passwords, credit card numbers, or personal information.
- Data Manipulation: Attackers can modify, delete, or insert records into the database.
- Privilege Escalation: In some cases, attackers can escalate their privileges by executing administrative SQL commands (e.g., DROP DATABASE or GRANT ALL PRIVILEGES).

## Differentiate XSS from CSRF

### XSS (Cross-Site Scripting)

Definition: XSS is a vulnerability that allows attackers to inject malicious scripts into webpages viewed by other users. These scripts can then execute in the victim’s browser, potentially stealing data (e.g., session cookies) or performing actions on behalf of the victim.

- Attack Type: Client-side attack.
- Example: Injecting JavaScript into a form or URL that will run in the victim’s browser.
- Mitigation: Input validation and output encoding, use of Content Security Policy (CSP), etc.

### CSRF (Cross-Site Request Forgery)

Definition: CSRF tricks an authenticated user into performing unwanted actions on a web application. It exploits the trust a website has in a user’s browser (session).

- Attack Type: Server-side attack.
- Example: If a user is logged into a banking site, an attacker could trick them into transferring money by sending a malicious request (using the victim’s credentials) from another website.
- Mitigation: Use of anti-CSRF tokens, SameSite cookie attribute, checking referer headers.

## Explain Man-in-the-Middle (MITM) Attacks

MITM Attack: In a man-in-the-middle attack, the attacker secretly intercepts and potentially alters the communication between two parties (such as a client and a server) without their knowledge.

**Examples**

- Intercepting unencrypted HTTP requests to read or modify sensitive data (like login credentials).
- Intercepting encrypted traffic by using techniques like SSL stripping or creating fake certificates.
- Mitigation: Use HTTPS, ensure the use of strong encryption (e.g., TLS), and validate certificates.

## What is a Server-Side Request Forgery (SSRF) attack?

SSRF occurs when an attacker is able to send malicious requests from the server-side to internal resources (e.g., databases, internal APIs).

- The attacker provides a URL to the server to access local or private network services.
- Example: Attacker sending a request like <http://localhost/admin> to access restricted resources.
- Mitigation: Validate and sanitize user input, block outgoing requests to internal or non-public services, and use firewalls to isolate sensitive endpoints.

## How is the padlock icon in the browser generated?

The padlock icon in the browser indicates that the conection is secure via HTTPS (SSL/TLS)

- Generated when the website presents a valid SSL/TLS certificate - which ensures encrypted communication.
- The certificate is verified by the browser to confirm the authenticity of the website.

## What is Same Origin Policy and CORS?

### Same Origin Policy

A security feature implemented by web browsers that restricts web pages from making requests to a domain different from the one that served the web page. It prevents malicious scripts from accessing data on a different domain.

### CORS (Cross-Origin Resource Sharing)

A mechanism that allows restricted resources on a web server to be requested from another domain. CORS is a relaxation of the Same Origin Policy, enabled by adding special headers to HTTP responses. Example: A website on example.com can use CORS to allow AJAX requests to an API hosted on api.example.com.
