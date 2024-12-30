# Web Application Security

## What’s a web app and how does it work?

A **web application** is a software application that runs on a web server and interacts with users through a web browser. It allows users to access and interact with data stored on the server over the internet. Web apps typically follow the **client-server model**, where:

- **Client**: The user's device that makes requests (e.g., browser).
- **Server**: The web server that processes requests and responds with appropriate data.

### How Web Apps Work

1. The client (browser) sends an HTTP/HTTPS request to the web server.
2. The web server processes the request and interacts with the database or application server.
3. The server sends back an HTTP response with the requested data (HTML, JSON, etc.).
4. The client renders the data on the screen.

## Different Types of Servers

1. **Web Server**

   - Hosts the web pages of a web application and serves HTTP requests. Example: Apache, Nginx.

2. **App Server**

   - Runs the application logic, often processing dynamic content. It can be separate from the web server. Example: Tomcat, Node.js.

3. **File Server**

   - Provides storage and access to files, serving them to clients. Example: Samba, FTP server.

4. **DB Server**
   - Hosts databases and manages requests for reading and writing data. Example: MySQL, PostgreSQL.

## OWASP Top 10

The **OWASP Top 10** is a list of the ten most critical web application security risks, published by the Open Web Application Security Project (OWASP). The latest list includes:

1. **Injection** (SQL, NoSQL, LDAP, etc.)
2. **Broken Authentication**
3. **Sensitive Data Exposure**
4. **XML External Entities (XXE)**
5. **Broken Access Control**
6. **Security Misconfiguration**
7. **Cross-Site Scripting (XSS)**
8. **Insecure Deserialization**
9. **Using Components with Known Vulnerabilities**
10. **Insufficient Logging and Monitoring**

## Injection Attacks

1. **SQL Injection**

   - Malicious SQL code inserted into a web application's query, compromising the database.

2. **LDAP Injection**

   - Injecting malicious LDAP queries, potentially bypassing authentication or accessing unauthorized data.

3. **NoSQL Injection**

   - Attacks on NoSQL databases by injecting malicious code into queries. Example: MongoDB.

4. **Blind SQL Injection**

   - A variant of SQL Injection where the attacker doesn't see the output but can infer information by sending payloads and observing server responses.

5. **XML Injection**

   - Manipulating XML data to exploit vulnerabilities in the processing of XML data.

6. **URL Injection**
   - Manipulating URL parameters to inject malicious data or bypass security measures.

## Broken Authentication and Session Management

- **Broken Authentication** occurs when attackers exploit weak authentication mechanisms to gain unauthorized access to systems. Common issues include weak passwords, session fixation, and credential stuffing.
- **Session Management** is the process of keeping track of user sessions. Poor session management can lead to session hijacking or fixation, allowing attackers to impersonate valid users.

## Sensitive Data Exposure

- Occurs when sensitive information, like passwords, credit card numbers, or personal details, are not protected during storage or transmission. Common causes include using weak encryption, transmitting data over insecure channels (HTTP instead of HTTPS), or improper key management.

## XML External Entities (XXE)

- **XXE attacks** exploit vulnerabilities in XML parsers, allowing attackers to access files on the server or perform DoS attacks.

  - **Billion Laughs Attack**: An XXE attack that causes exponential growth of XML data, overwhelming the server’s resources and causing denial of service.

## Broken Access Control

- Refers to weaknesses in a system's access control mechanism, allowing unauthorized users to access resources or perform actions outside their permission level. Common issues include missing user role validation or improper URL access control.

## Security Misconfiguration

- Happens when systems are not securely configured. This could include leaving default settings, exposing unnecessary services, or using weak encryption algorithms. Regular audits and security best practices can mitigate this risk.

## Using Components with Known Vulnerabilities

- Using outdated or unpatched libraries, frameworks, or software components with known vulnerabilities. Attackers can exploit these vulnerabilities to compromise the system.

## Cross-Site Scripting (XSS)

1. **Stored XSS**

   - Malicious scripts are stored on the server and then served to all users who visit a vulnerable page.

2. **Reflected XSS**

   - Malicious scripts are reflected off the web server and executed on a user’s browser when they click a specially crafted link.

3. **DOM-based XSS**
   - The vulnerability exists in the client-side code, typically JavaScript, which modifies the DOM and executes malicious scripts.

## CSRF (Cross-Site Request Forgery)

- **CSRF** attacks trick a user into executing unwanted actions on a web application where they are authenticated. This can lead to actions like transferring funds or changing account settings without the user's consent.

  - **SSRF (Server-Side Request Forgery)**
    - A type of attack where the attacker sends a request to an internal server, usually bypassing firewalls or other security controls.

## Insecure Deserialization

- Insecure deserialization occurs when untrusted data is deserialized into an object, potentially allowing attackers to execute arbitrary code or perform other malicious actions.

## Insufficient Logging and Monitoring

- Insufficient logging makes it difficult to detect and respond to security breaches. Proper logging should track access, errors, and anomalous activities, and be monitored for suspicious behavior.

## Threat Modeling

1. **STRIDE**

   - A threat modeling framework to identify potential threats: **Spoofing**, **Tampering**, **Repudiation**, **Information Disclosure**, **Denial of Service**, and **Elevation of Privilege**.

2. **DREAD**
   - A threat rating model used to assess risk: **Damage**, **Reproducibility**, **Exploitability**, **Affected Users**, and **Discoverability**.

## SAST and DAST

1. **SAST (Static Application Security Testing)**

   - Analyzes the source code of an application to find vulnerabilities before it’s run (at rest).

2. **DAST (Dynamic Application Security Testing)**
   - Analyzes the application during runtime to detect vulnerabilities that could be exploited while the application is active.

## What’s a WAF (Web Application Firewall)?

- A **WAF** is a security device or software that filters and monitors HTTP traffic between a web application and the Internet. It helps protect against attacks like SQL injection, XSS, and CSRF by filtering out malicious traffic before it reaches the application.

## Reverse and Forward Proxy

1. **Forward Proxy**

   - Sits between the client and the internet, forwarding requests from clients to the server and vice versa. It hides the client's identity.

2. **Reverse Proxy**
   - Sits between the client and the server and forwards requests to backend servers. It often performs load balancing, caching, and security functions.

## HTTP Security Headers

1. **HSTS (HTTP Strict Transport Security)**

   - Instructs browsers to only communicate with the server over HTTPS, preventing man-in-the-middle attacks.

2. **Cache-Control: no-cache**

   - Prevents the browser from caching sensitive data, ensuring that fresh data is retrieved on each request.

3. **Content Security Policy (CSP)**

   - Mitigates XSS risks by specifying which dynamic resources are allowed to load on the webpage.

4. **CORS (Cross-Origin Resource Sharing)**

   - Defines which external domains are allowed to access resources from the server, preventing unauthorized cross-origin requests.

5. **X-Frame-Options**

   - Prevents the page from being embedded in a frame or iframe, helping protect against clickjacking attacks.

6. **X-XSS-Protection**

   - Enables the browser’s built-in protection against reflected XSS attacks.

7. **Access-Control-Allow-Origin**
   - Specifies which domains are allowed to make cross-origin requests to the server.

## Code Vulnerability: Weak vs Strong Code

- **Weak Code**

  - Contains poor security practices, such as hardcoded credentials, improper error handling, and lack of input validation. It is prone to exploitation.

- **Strong Code**
  - Follows secure coding practices, such as input validation, proper error handling, using encryption, and ensuring that data is sanitized before processing.
