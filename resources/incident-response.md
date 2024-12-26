# Incident Response

## What are the key elements of a security incident response plan?

A security incident response plan outlines the steps an organization will take when a security breach or incident occurs. The key elements include:

- **Preparation**: Identifying assets, creating a response team, and setting up necessary tools (e.g., monitoring systems).
- **Detection**: Monitoring for signs of a security incident and identifying it.
- **Containment**: Isolating affected systems to prevent the spread of the attack.
- **Eradication**: Identifying the root cause and removing the threat.
- **Recovery**: Restoring systems and data, ensuring they are free of vulnerabilities.
- **Lessons learned**: After the incident, reviewing the response and updating the plan to improve future responses.

## Several employees received a phishing email and one clicked on the link. How do you respond?

- **Identify the Scope**
  - Use the email logs to identify all employees who received the phishing email.
  - Check if any credentials were entered on the phishing site or if malware was downloaded.
- **Containment**
  - Block the phishing URL at the proxy/firewall level.
  - Reset credentials for any employees who entered their login information.
- **Eradication**
  - Scan systems of affected users for malware or suspicious activity.
  - Remove any malicious attachments or files.
- **Recovery**
  - Ensure all affected accounts and systems are secure.
  - Notify impacted users and provide guidance on spotting phishing emails.
- **Lessons Learned**
  - Conduct a phishing awareness campaign.
  - Enable MFA (if not already in place) to reduce the risk of compromised accounts.

## Your website is experiencing a Distributed Denial of Service (DDoS) attack. How do you mitigate it?

- **Immediate Action**
  - Redirect traffic through a DDoS mitigation service like Cloudflare.
  - Identify attack patterns (e.g., IPs, payloads) and block them at the firewall.
- **Investigation**
  - Work with ISPs to trace the source of the attack.
  - Determine if the attack is a distraction for a more targeted breach.
- **Response**
  - Ensure critical services are operational using failover mechanisms.
  - Increase server capacity temporarily if possible.
- **Post-Attack Measures**
  - Implement rate-limiting and Web Application Firewalls (WAF).
  - Review logs to refine detection and response strategies.
