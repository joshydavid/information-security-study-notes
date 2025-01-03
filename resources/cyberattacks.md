# Cyberattacks

## Define the terms Virus, Malware, and Ransomware

### Virus

A program that replicates itself and spreads to other files or systems, often causing harm.

### Malware

A broader term encompassing any malicious software that disrupts or gains unauthorized access to computer systems.

### Ransomware

A malicious software encrypting files or computer systems and requesting a ransom for their decryption.

###

## Define the terms Threat vs Vulnerability vs Risk

### Threat

A threat is a potential danger that exploits a vulnerability and cause harm to a system. It requires a vulnerability to exist for it pose a risk.

E.g a cybercriminal attempting to steal sensitive data.

### Vulnerability

A vulnerability is a weakness or flaw in a system that could be exploited by a threat to compromise confidentality, integrity, or availability.

E.g software with known security bugs, weak/reused password, outdated dependencies in a React app

### Risk

A risk is the likelihood and impact of a threat exploiting a vulnerability resulting in potential harm.

E.g.

- If an outdated library (vulnerability) in your React app is exposed on the internet and a hacker (threat) exploits it, it could lead to a data breach (impact).
- The risk of a ransomware attack encrypting critical data due to unpatch systems, the risk of insider threats leaking sensitive data.

## Common Types of Cyberattacks

### Social Engineering

Social engineering attacks involve manipulating people into revealing sensitive information or performing actions that can compromise security. These attacks often exploit human psychology rather than technical vulnerabilities.

**Common Types of Social Engineering Attacks**

- Phishing

  - A type of attack where attackers impersonate legitimate organizations or individuals to trick victims into revealing personal information, such as usernames, passwords, or credit card details.
  - Common Methods:
    - Fake emails or websites that look like those from banks, social media platforms, or tech companies.
    - Malicious links or attachments that install malware.

- Spear Phishing

  - A more targeted form of phishing. Attackers customize the message to a specific individual or organization, often using information gathered from social media or other sources to make the message seem more legitimate.
  - Example: An attacker might send an email that appears to come from a trusted colleague, asking the victim to click on a link or download an attachment.

- Vishing (Voice Phishing)

  - Involves phone calls where attackers impersonate legitimate entities (e.g., banks, government agencies, or technical support) to extract sensitive information.
  - Common Tactics:
    - Automated robocalls asking for credit card information.
    - Fraudulent calls that claim the victim’s account has been compromised and ask them to provide personal information to “resolve” the issue.

- Smishing (SMS Phishing)

  - A type of phishing where attackers use text messages (SMS) to trick victims into clicking on malicious links or providing personal information.
  - Example: A text message claiming to be from a bank, asking the victim to log in to a fake website using a provided link.

- Pretexting

  - The attacker creates a fabricated story or pretext to obtain information from the victim. This often involves impersonating someone who has a legitimate reason to request information (e.g., a co-worker, law enforcement, or a contractor).
  - Example: A hacker might pose as an IT technician calling to “fix” an issue on your computer, asking you for your username and password.

- Baiting

  - In this attack, the attacker offers something enticing to the victim, such as free software, gifts, or media files, to persuade them to download malware or provide personal information.
  - Example: A USB drive left in a public place with a label like “Confidential – Do Not Open” to tempt someone into plugging it into their computer, which could install malware.

- Quizzes and Surveys

  - Attackers use seemingly harmless quizzes or surveys to gather personal information that can be used for further attacks.
  - Example: A Facebook quiz that asks for answers to security questions (e.g., “What was the name of your first pet?”).

- Whaling

  - A type of spear phishing targeting high-profile individuals, such as executives or key personnel in an organization, to steal sensitive corporate information or money.
  - Example: An attacker might impersonate a company’s legal department or a trusted business partner to request wire transfers or access to private data.

- Shoulder Surfing

  - This involves directly observing someone’s sensitive information, such as passwords or PINs, by watching them type on a keyboard or viewing their screen.
  - Example: An attacker may observe a person entering their password on a public computer or smartphone in a crowded place.

- Tailgating
  - Attackers gain unauthorized physical access to a restricted area by following an authorized person into the premises without their knowledge or consent.
  - Example: An attacker might walk behind an employee into a secure building, using their access badge to slip past security.

**Prevention**

- Education and Awareness: Regularly train employees to recognise all the threats above
- Two-factor Authentication (2FA): Implementing 2FA makes it more difficult for attackers to gain unauthorized access even if they obtain login credentials.
- Verify Request: Always verify sensitive requests (like money transfers or confidential information) through a trusted channel, such as phone calls.
- Limit Information Sharing: Be cautious about what personal or organizational information is shared publicly (on social media, websites, etc.), as attackers can use this data to craft convincing attacks.
- Report Suspicious Activity: Encourage employees to report any suspicious emails, phone calls, or requests immediately.

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

## How would you respond if your site is being targetted by a DDoS attack?

DDoS attack impacts the availability of a service, it's important to identify and mitigate the attack to ensure minimal disruptions to users.

- Use networking monitor tools such as IDS to detect unusual traffic patterns for example sudden spike in requests/traffics from a specific geographic location or IP range.
- Identify the type of DDoS attack - volume-based attack like UDP floods, protocol attack like SYN flood or application layer attack like HTTP flood as understanding the attack will help in applying the appropriate mitigation techniques.
- Mitigate the attack by rate-limiting or throttling requests to prevent overloading the servers.
- Use a Web Application Firewall (WAF) to filter malicious traffic and block suspicious IPs or regions if needed. (Layer 7)
- Use Content Delivery Network (CDN) to absorb traffic and prevent overload on my infrastructure.
- Enable IP blacklisting or geo-blocking to reduce the attack surface. (Layer 3/4, Network/Transport Layer)
- Keep the internal teams informed—working closely with the network security team, DevOps, and customer service. If necessary, I’d notify users and customers about the situation, providing updates on the resolution process.
- Once attack is cover, conduct a post-mortem analysis to understand how the attack occurred and what could have been done differently.

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
