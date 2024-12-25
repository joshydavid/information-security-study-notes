# Information Security Interview Preparation (Cyberattacks)

## Threat vs Vulnerability vs Risk

### Threat

A threat is anything that has the potential to exploit a vulnerability and cause harm to a system. It represents a potential danger, and requires a vulnerability to exist for it pose a risk.

E.g a cybercriminal attempting to steal sensitive data.

### Vulnerability

A vulnerability is a weakness or flaw in a system that can be exploited by a threat to cause harm.

E.g software with known security bugs, weak/reused password

### Risk

A risk is the potential for loss or damage when a threat exploits a vulnerability, it's the likelihood and impact of harm occurring.

E.g. The risk of a ransomeware attack encrypting critical data due to unpatch systems, the risk of insider threats leaking sensitive data.

## Common Types of Cyberattacks

### Social Engineering

An attacker manipulates individuals into giving up sensitive information or performing actions.

- E.g. Pretending to be IT support to gain passwords over a phone call.
- Mitigation:
  - Conduct security awareness training.
  - Implement strict verification protocols.
  - Use MFA to reduce the impact of compromised credentials.

### Phishing

An attacker tricks individuals into revealing sensitive information, such as passwords or financial data, by masquerading as a trusted entity.

- E.g. Fake emails or websites resembling legitimate ones to steal credentials.
- Mitigation:
  - Implement email filtering and anti-phishing tools.
  - Train employees to recognize phishing attempts.
  - Use Multi-Factor Authentication (MFA) to protect accounts.

### SQL Injection

An attacker inserts malicious SQL code into a database query to manipulate or extract data.

- E.g. Entering ' OR '1'='1 into a login field to bypass authentication.
- Mitigation:
  - Use parameterized queries and prepared statements.
  - Validate and sanitize user inputs.
  - Implement Web Application Firewalls (WAF).

### Cross-Site Scripting (XSS)

An attacker injects malicious scripts into websites, which are then executed in users’ browsers.

- E.g. A comment field on a website is exploited to inject malicious JavaScript.
- Mitigation:
  - Sanitize and escape user inputs.
  - Use Content Security Policy (CSP).
  - Validate outputs before rendering them in the browser.

### Ransomware

Malware encrypts data, and attackers demand payment for the decryption key.

- E.g. WannaCry ransomware attacks on healthcare systems.
- Mitigation:
- Regularly back up data and keep backups offline.
- Patch software and update systems to fix vulnerabilities.
- Use endpoint protection solutions to detect malicious activity.

### Privilege Escalation

An attacker gains unauthorized access to higher privileges within a system.

- E.g. Exploiting a bug to access admin-level accounts.
- Mitigation:
  - Follow the principle of least privilege (PoLP).
  - Regularly patch vulnerabilities.
  - Use access controls and audit logs to monitor privilege changes.

### Zero-Day Exploits

An attacker exploits a vulnerability before it’s discovered or patched by the vendor.

- E.g. Exploiting unpatched bugs in software like web browsers.
- Mitigation:
  - Use behavior-based threat detection tools.
  - Update software frequently.
  - Monitor threat intelligence sources for early warnings.

### Insider Threats

Malicious or negligent insiders misuse their access to systems or data.

- E.g. An employee downloading sensitive data before resigning.
- Mitigation:
  - Monitor and log user activity.
  - Enforce role-based access controls (RBAC).
  - Conduct regular security audits.

## How would you defend against a DDoS attack?

Distributed Denial of Service (DDoS) attacks overwhelm a network or service with excessive traffic to cause disruptions. To defend against a DDoS attack:

- **Traffic filtering** Use firewalls and intrusion prevention systems (IPS) to detect and block malicious traffic.
- **Content Delivery Networks (CDNs)**: Use CDNs to distribute traffic across multiple servers and reduce the load on the origin server.
- **Rate limiting**: Implement rate limiting to restrict the number of requests a server will respond to from a single source.
- **Geo-blocking**: Block traffic from regions that are not relevant to the business.
- **Scrubbing centers**: Redirect traffic to a specialized DDoS mitigation service that can clean the traffic before it reaches the target.

## Explain the concept of a Man-in-the-Middle (MITM) attack and how to mitigate it

Man-in-the-Middle (MITM) attack occurs when an attacker intercepts and potentially alters the communication between two parties without their knowledge.
E.g An attacker might intercept communication between a user and a website (e.g., over HTTP) and steal sensitive data like login credentials.

**Mitigation**

- Use HTTPS (SSL/TLS): Always use encrypted communication channels to prevent interception.
- Certificate pinning: Ensure that the server’s certificate is verified against a known, trusted one to prevent fake certificates from being used.
- Public Key Infrastructure (PKI): Implement strong certificate authorities (CAs) to verify identities.
