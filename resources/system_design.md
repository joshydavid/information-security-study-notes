# Information Security Interview Preparation (System Design)

## How would you secure an API service that handles sensitive user data?

1. Use HTTPS for secure communication.
2. Implement OAuth 2.0 or JWT for secure and scalable authentication.
3. Validate and sanitize all inputs to prevent injection attacks.
4. Use strong encryption (AES-256) for sensitive data storage.
5. Implement rate-limiting and IP whitelisting to prevent brute force and DDoS attacks.

## How would you design a secure online banking system from the ground up?

1. Authentication: Implement multi-factor authentication (MFA) for user logins.
2. Encryption: Use SSL/TLS for all communications and AES for sensitive data storage.
3. Authorization: Use role-based access control (RBAC) to ensure users have appropriate permissions.
4. Session Management: Implement session timeouts and refresh tokens.
5. Logging and Monitoring: Set up logging for all actions, and use intrusion detection systems to detect abnormal activity.
6. Regular Audits: Perform regular security audits and vulnerability assessments.

## Pentration testing tools

- Nmap: For network scanning and discovery.
- Burp Suite: For web application security testing (great for exploiting vulnerabilities like XSS, CSRF, SQL injection).
- Metasploit: For exploitation of known vulnerabilities.
- Wireshark: For packet capturing and analysis.
- Nikto: For web server scanning.
