# Scenarios

**NIST 800-61 Incident Response Lifecycle**

The NIST framework divides incident response into four main phases:

1. Preparation
   • Focuses on readiness (tools, processes, and policies).
   • Example: Ensuring logging, incident response plans, and team training are in place.
2. Detection and Analysis
   • Identifying the incident and assessing its scope and impact.
   • Example: Using SIEM tools, IDS/IPS, and threat intelligence to detect anomalies.
3. Containment, Eradication, and Recovery
   • Contain the threat, remove it, and restore normal operations.
   • Example: Isolate the compromised server, patch the vulnerability, and recover from backups.
4. Post-Incident Activity
   • Learn from the incident and improve future defenses.
   • Example: Conduct a root cause analysis and update security controls.

## [Incident Response] A server has been compromised, and attackers are exfiltrating sensitive data. How would you handle the situation?

- Understand incident response steps (identification, containment, eradication, recovery, lessons learned).
- Knowledge of monitoring tools (SIEMs, IDS/IPS)
- Prioritization and decision-making under pressure.

**How to answer?**

1. Identify the scope of the attack (logs, alerts, impacted systems).
2. Contain the breach (e.g., isolate affected servers, revoke credentials).
3. Eradicate the threat (e.g., patch vulnerabilities, remove malware).
4. Recover and restore systems (e.g., clean backups).
5. Conduct a post-mortem (e.g., root cause analysis, improve controls).

## [Threat Modelling] You’re tasked with securing a new API that handles sensitive customer data. What threats would you anticipate, and how would you mitigate them?

- Ability to identify potential threats (STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privileges).
- Familiarity with security controls (encryption, rate limiting, input validation).

**Threats**

- SQL injection
- Broken authentication (e.g., session hijacking)
- Data exposure (e.g., plaintext transmission)

**Mitigations**

- Use parameterized queries to prevent SQL injection.
- Implement OAuth 2.0 for secure authentication.
- Use HTTPS and encrypt sensitive fields at rest.

## [Security Architecture Reviews] Your team is designing a multi-tier web application. How would you secure the architecture?

- Knowledge of secure software and network architecture.
- Application of defense-in-depth principles.

**Frontend**

- Sanitize and validate user inputs to prevent XSS.
- Enforce Content Security Policy (CSP).

**Backend**

- Use access control to limit API endpoints.
- Store passwords using strong hashing algorithms like Argon2 or bcrypt.

**Database**

- Enable encryption for sensitive data (e.g., AES-256).
- Implement least-privilege access for database users.

**Networking**

- Deploy a Web Application Firewall (WAF).
- Deploy IDS/IPS.
- Restrict access with VPCs and security groups.
- Use TLS for secure communication.

## [Vulnerability Assessment] You’ve been informed of a critical vulnerability in an open-source library used in production. What’s your process for addressing it?

Awareness of CVEs, patch management, and risk prioritization.

- Assess the library’s impact on the application (where and how it’s used).
- Determine the severity of the vulnerability (CVSS score, exploitability).
- Check for available patches or mitigations.
- Apply the patch in a staging environment, test, and deploy to production.
- Monitor for any abnormal activity post-deployment.

## [Phishing Attack] Your organization experiences a phishing attack where an employee unknowingly provides their credentials to an attacker. What steps would you take?

Awareness of social engineering risks and steps to mitigate compromised accounts.

- Disable the compromised account immediately.
- Inform affected teams and stakeholders.
- Perform an investigation (e.g., check logs for unauthorized access).
- Reset all related credentials and enforce 2FA for added security.
- Educate employees on phishing awareness (e.g., spotting suspicious emails).

## [Ransomware Attack] A ransomware attack locks critical systems, and the attackers demand payment. What would you do?

Incident handling, disaster recovery, and backup strategies.

- Isolate infected systems to prevent spread.
- Identify the ransomware strain and determine if decryption tools exist.
- Restore from clean backups (if available).
- Notify legal and regulatory bodies, as appropriate.
- Review security posture and implement additional controls (e.g., endpoint protection).

## [Insider Threat] A malicious insider is suspected of stealing intellectual property. How would you investigate?

- Understanding of insider threat detection and monitoring.
- Ability to handle sensitive situations discreetly.

**Investigation**

- Use DLP (Data Loss Prevention) tools to monitor data exfiltration.
- Review access logs for suspicious behavior (e.g., accessing unrelated projects).
- Restrict access to critical systems for the suspect while investigating.
- Work with HR and legal teams to take appropriate action.

## [Zero-Day Exploit] A zero-day vulnerability is discovered in a widely used component of your infrastructure. How do you mitigate the risk until a patch is released?

Ability to implement short-term mitigations and maintain business continuity.

- Identify and isolate affected systems.
- Apply available mitigations (e.g., disable vulnerable features, restrict access).
- Monitor for any exploitation attempts (SIEM tools, logs).
- Work closely with the vendor for updates and patch deployment.

## [Security in SDLC] How would you ensure that security is integrated into the software development lifecycle (SDLC)?

Knowledge of secure development practices and DevSecOps.

- Requirements: Identify security requirements (e.g., encryption, authentication).
- Design: Perform threat modeling (e.g., STRIDE).
- Implementation: Enforce secure coding standards (e.g., OWASP Top 10).
- Testing: Use static/dynamic analysis tools (e.g., SAST, DAST).
- Deployment: Implement CI/CD with security checks.
- Monitoring: Continuously monitor for vulnerabilities post-deployment.

## [Cloud Security] Your team is migrating an application to the cloud. What steps would you take to ensure it’s secure?

- Secure credentials with IAM roles and enforce least-privilege access.
- Enable encryption for data in transit (SSL/TLS) and at rest (e.g., S3 bucket encryption).
- Monitor for misconfigurations with tools like AWS Config or Azure Security Center.
- Enable logging and monitoring (e.g., CloudTrail, GuardDuty).
- Conduct a security assessment before deployment.

## How would you handle a DDoS attack?

A DDoS (Distributed Denial of Service) attack occurs when an attacker uses multiple compromised systems to flood a target system with traffic, overwhelming its capacity to handle requests, and making the service unavailable.

1. Detection
   - Use traffic analysis tools (networking monitoring) to identify unusual spikes in traffic.
   - Look for characteristics of DDos attack, such as sudden surge in traffic from a single/multi IP address
2. Containment
   - Rate Limiting: Reduces the impact by limiting the number of request a user can make within X duration.
   - Geo-blocking: Block traffic from specific geographic regions that are not relevant to the service
   - Blackholing: Redirect malicious traffic to a "black hole", blocking it from reaching the target server.
3. Mitigation
   - Use Content Delivery Network (CDN) like Cloudflare, it helps to absorb the traffic and prevent it from hitting the actual server.
   - Engage DDoS mitigation service from ISP
   - Network filtering, use Web Application Firewalls (WAFs) or Intrusion Prevention System (IPS) to filter malicious traffic
4. Recovery
   - Restore service fully and monitor the situation
   - Apply configuration changes to strengthen defenses
5. Post-Incident Review
   - Perform post-mortem analysis to understand how the attack happened and how it was conducted.
   - Update incident response procedure.

## If a company’s server was compromised and sensitive data was leaked, what steps would you take to mitigate the damage and prevent future breaches?

1. Contain the breach: Immediately disconnect the compromised server from the network.
2. Identify the scope: Assess what data was leaked and identify the vulnerability.
3. Communicate: Notify affected stakeholders and regulatory bodies if required.
4. Fix the vulnerability: Apply patches or fix the weaknesses that allowed the breach.
5. Monitor for further issues: Increase monitoring to detect any new attacks or exploits.
6. Review and update security policies: Perform a thorough post-incident review to strengthen security measures.

## You discover that an employee has been using weak passwords across multiple accounts, and one of their accounts has been compromised. What actions would you take?

1. Reset passwords immediately on all affected accounts.
2. Enforce stronger password policies, such as a minimum length, complexity, and multi-factor authentication.
3. Conduct a security training session for the employee to emphasize password best practices.
4. Perform a security audit to check if any other accounts were compromised.

## Imagine you are developing a new feature that stores sensitive user data. What security measures would you implement to protect this data?

- Use Secure Development Practices

  - Follow Secure Development Lifecycle practices.
  - Conduct code reviews to ensure no hardcoded secrets such as API keys or passwords left in the source code
  - Store secrets such as API keys or environment variables securely

- Access Control

  - Implement Role-Based Access Control (RBAC) or Attribute-Based Access Control (ABAC) to restrict data access based on user roles and permissions.
  - Enforce the Principle of Least Privilege (PoLP): Grant users and systems the minimum necessary access.
  - Use time-limited or context-aware access tokens to further restrict access.

- Implement API Security

  - Use secure API design principles such as authentication using OAuth2
  - Rate-limit API calls to prevent Denial-of-Service (DoS) attacks
  - Valid all input data received by the API to prevent code injection attacks (SQL injection, XSS)
  - Use libraries or frameworks that support parameterized queries or prepared statements to interact with databases.

- Data Minimization and Anonymization

  - Only collect and store the data necessary for the feature to function. Avoid collecting excessive or unnecessary data.
  - Use pseudonymization or anonymization techniques where applicable to reduce the risk of exposing identifiable information.

- Data Encryption

  - At Rest: Use strong encryption algorithm (AES-256) to encrypt sensitive data
  - In Transit: Use TLS to encrypt data as it travels from client to server
  - Key Management: Implement secure key management practices, such as using a hardware security module (HSM) or key vault, to protect encryption keys.

- Authentication and Authorization

  - Require strong passwords and enforce password policies (e.g., length, complexity, rotation).
  - Use Multi-Factor Authentication (MFA) to add an extra layer of security.
  - Secure session tokens with HttpOnly, Secure, and SameSite flags in cookies to prevent hijacking.

- Regular Security Testing

  - Conduct penetration testing to identify vulnerabilities in the feature.
  - Perform static and dynamic application security testing (SAST/DAST) as part of your development pipeline.
  - Use automated tools to scan for vulnerabilities in dependencies and libraries.

- Incident Response Plan

  - Develop an incident response plan in case of data breaches or security incidents.
  - Regularly test the plan through drills to ensure rapid response and mitigation of potential risks.

- Logging and Monitoring
  - Implement logging for access attempts, modifications, and suspicious activities.
  - Use a Security Information and Event Management (SIEM) solution to monitor logs for anomalies and potential breaches.
