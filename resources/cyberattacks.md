# Information Security Interview Preparation (Cyberattacks)

## How would you defend against a DDoS attack?

Distributed Denial of Service (DDoS) attacks overwhelm a network or service with excessive traffic to cause disruptions. To defend against a DDoS attack:

• **Traffic filtering** Use firewalls and intrusion prevention systems (IPS) to detect and block malicious traffic.
• **Content Delivery Networks (CDNs)**: Use CDNs to distribute traffic across multiple servers and reduce the load on the origin server.
• **Rate limiting**: Implement rate limiting to restrict the number of requests a server will respond to from a single source.
• **Geo-blocking**: Block traffic from regions that are not relevant to the business.
• **Scrubbing centers**: Redirect traffic to a specialized DDoS mitigation service that can clean the traffic before it reaches the target.

## Explain the concept of a Man-in-the-Middle (MITM) attack and how to mitigate it

Man-in-the-Middle (MITM) attack occurs when an attacker intercepts and potentially alters the communication between two parties without their knowledge.
E.g An attacker might intercept communication between a user and a website (e.g., over HTTP) and steal sensitive data like login credentials.

**Mitigation**
• Use HTTPS (SSL/TLS): Always use encrypted communication channels to prevent interception.
• Certificate pinning: Ensure that the server’s certificate is verified against a known, trusted one to prevent fake certificates from being used.
• Public Key Infrastructure (PKI): Implement strong certificate authorities (CAs) to verify identities.
