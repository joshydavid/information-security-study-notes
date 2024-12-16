# Information Security Interview Preparation (Scenarios)

## Scenarios

### How would you handle a DDoS attack?

A DDoS (Distributed Denial of Service) attack occurs when an attacker uses multiple compromised systems to flood a target system with traffic, overwhelming its capacity to handle requests, and making the service unavailable.

1. Detection
   - Use traffic analysis tools (networking monitoring) to identify unusual spikes in traffic.
   - Look for characteristics of DDos attack, such as sudden surge in traffic from a single/multi IP address
2. Containment
   - Rate Limiting: Reduces the impact by limiting the number of request a user can make within X duration.
   - Geo-blocking: Block traffic from specific geographic regions that are not relevant to the service
   - Blackholing: Redirect malicious traffic to a "bllack hole", blocking it from reaching the target server.
3. Mitigation
   - Use Content Delivery Network (CDN) like Cloudflare, it helps to absorb the traffic and prevent it from hitting the actual server.
   - Engage DDoS mitigation service from ISP
   - Network filtering, use Web Application Firewalls (WAFs) or Intrusion Prevention System (IPS) to filter malicious traffic
4. Recovery
   - Restore service fully and monitor the situation
   - Apply configuration changes to strengthen defenses
5. Post-Incident Review
   - Perform post-morterm analysis to understand how the attack happened and how it was conducted.
   - Update incident response procedure.

### If a company’s server was compromised and sensitive data was leaked, what steps would you take to mitigate the damage and prevent future breaches?

1. Contain the breach: Immediately disconnect the compromised server from the network.
2. Identify the scope: Assess what data was leaked and identify the vulnerability.
3. Communicate: Notify affected stakeholders and regulatory bodies if required.
4. Fix the vulnerability: Apply patches or fix the weaknesses that allowed the breach.
5. Monitor for further issues: Increase monitoring to detect any new attacks or exploits.
6. Review and update security policies: Perform a thorough post-incident review to strengthen security measures.

### You discover that an employee has been using weak passwords across multiple accounts, and one of their accounts has been compromised. What actions would you take?

1. Reset passwords immediately on all affected accounts.
2. Enforce stronger password policies, such as a minimum length, complexity, and multi-factor authentication.
3. Conduct a security training session for the employee to emphasize password best practices.
4. Perform a security audit to check if any other accounts were compromised.

### Imagine you are developing a new feature that stores sensitive user data. What security measures would you implement to protect this data?

- Use Secure Development Practices

  - Follow Secure Development Lifecycle practices.
  - Conduct code reviews to ensure no hardcoded secrets such as API keys or passwords left in the sourcecode
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
