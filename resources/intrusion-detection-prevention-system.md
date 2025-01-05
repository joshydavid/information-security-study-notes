# Intrusion Detection and Prevention System

## Intrusion Detection System (IDS)

- System designed to monitor and analyze network traffic for signs of security breaches, malicious activities, or policy violations.
- Does not block traffic (this is firewall)
- Deployed parallel to network traffic, analyses a copy of the traffic and does not directly interact with it.
- Passive, requires the intervention of the security team.
- Saves logs to SIEM system like Splunk.

## Types of Intrusion Detection System (IDS)

### Network-based IDS (NIDS)

- Monitors traffic on a network
- Deployed at critical points (routers, firewalls)
- Use case
  - Detect abnormal traffic patterns
  - DoS attacks
  - Protocol misuse

### Host-based IDS (HIDS)

- Monitors activity on a specific host/device
- Tracks system logs, file changes and process activity
- Use case
  - Detect file integrity issues
  - Unauthorized changes
  - Privilege escalations

### Hybrid IDS

Combines the strengths of both network-based and host-based IDS

## Intrusion Prevention System (IPS)

- System that monitors, analyses and blocks malicious traffics in real-time.
- Basically IDS + ability to block malicious traffics
- Additional layer behind firewall, deployed directly in the path of network traffic
- Active, does not require the intervention of the security team.
- E.g Inline firewalls with IPS functionality
- "Undercover security guard inside the building" (dynamic) while firewall is the security guard at the entrance (static - blocks based on pre-defined rules)

## Types of Intrusion Prevention System (IPS)

### Network-based IPS (NIPS)

- Monitors traffic on a network
- Positioned behind firewalls
- Use case -> detects and blocks exploits such as DDoS, worms, or unauthorized attempts

### Host-based IPS (HIPS)

- Installed directly on individual host (server) to monitor and protect them
- Monitor application behavior and protect against any malware by blocking them

## Detection Methods

### Signatured-based Detection

- Uses pre-defined patterns of known attacks
- Effective for known threats but weak against zero-day attacks (never seen before)

### Anomaly-based Detection

- Monitor whether traffics deviate from the normal behavior
- Effective for unknown threats, but prone to false positives

### Hybrid Detection

- Combines both signature-based and anomaly-based methods
- Balances accuracy and ability to detect unknown threats

## Key Components of IDS

1. Traffic Monitoring
   - Network-based IDS analyses packets at the network level.
   - Host-based IDS examines system logs, file systems and process activity.
2. Detection Engine
   - Applies detection rules (signature - pre-defined) or models (anomaly detection) to identify threats.
3. Alerting System
   - Sends notification or logs suspicious activity
   - Integrate with SIEM tools for correlation and reporting
4. Response Mechanism
   - IDS is passive and does not block threats, it only monitors behaviors.
   - Alerts administrators for manual intervention.

## Common Attacks Detected by IDS

- Denial of Service (DoS):
  - Abnormal spikes in traffic can indicate a DoS or DDoS attack.
- SQL Injection:
  - Monitors for suspicious queries or patterns in web traffic.
- Cross-Site Scripting (XSS):
  - Detects suspicious JavaScript payloads in HTTP traffic.
- Man-in-the-Middle (MITM):
  - Flags anomalies in SSL/TLS handshakes or unauthorized packet interception.
- Reconnaissance (Scanning):
  - Detects port scans or enumeration attempts by attackers.

## Challenges with IDS

- Volume of alerts: this can overwhelm security teams.
- Encrypted traffic: IDS tools struggle to inspect HTTPS traffic.
- Zero-Day threats: Signature-based IDS cannot detect new vulnerabilities since it learns from a pre-defined pattern.

## Challenges with IPS

- Volume of alerts: this can overwhelm security teams.
- Performance Impact: IPS are placed in-line with network traffic to perform deep packet inspection, this can lead to latency and performance degradation.
- Encrypted traffic: IDS tools struggle to inspect HTTPS traffic.
- Zero-Day threats: Signature-based IDS cannot detect new vulnerabilities since it learns from a pre-defined pattern.

## Scenario 1 - IDS vs IPS Deployment

**Your organization has recently experienced multiple SQL injection attempts on its web application. The security team is debating whether to deploy an IDS or an IPS. Which would you recommend, and why?**

- IDS

  - If the primary goal is monitoring and alerting, deploy an IDS to analyze traffic and provide visibility into SQL injection attempts.
  - IDS is less likely to disrupt legitimate traffic but requires a team to respond to alerts.

- IPS
  - If the goal is real-time prevention, deploy an IPS that can block SQL injection attempts actively.
  - Highlight the risk of false positives potentially blocking legitimate user requests.

For critical applications where response time is crucial, recommend an IPS; otherwise, consider combining both IDS (for monitoring) and IPS (for active protection).

## Scenario 2 - Signature vs Anomaly Detection

**An organization reports that their IDS flagged a sudden spike in traffic from a known IP address, but no malicious signatures were found. What detection method should they use to address such issues in the future?**

- The organization should consider implementing anomaly-based detection in their intrusion detection system (IDS) to address such issues in the future.
- Unlike signature-based detection, anomaly-based detection identifies deviations from established normal behavior patterns, such as unusual spikes in traffic volume.
- Zero-Day Threats - It can detect unknown or emerging threats that do not yet have defined signatures.
- It helps flag unusual traffic patterns, even if they don’t match known malicious signatures, which is crucial in identifying potentially stealthy or evolving attacks.
- However, this approach may lead to false positives, so combining it with signature-based detection (hybrid detection) might provide a balanced solution.

## Scenario 3 - False Positives in IPS

**Your IPS is blocking legitimate web traffic from an internal server, causing disruption to business operations. What steps would you take to resolve this issue?**

1. Investigate the Logs:
   - Check IPS logs to identify the specific rule or pattern that caused the block.
2. Analyze Traffic:
   - Determine if the traffic matches a malicious signature or if it was misclassified (false positive).
3. Update Rules/Policies:
   - Modify or fine-tune IPS rules to exclude the legitimate traffic from being blocked (e.g., adding a whitelist).
4. Test Changes:
   - Ensure that the adjustment doesn’t introduce new vulnerabilities or allow malicious traffic.
5. Monitor Closely:
   - Monitor the IPS to confirm that legitimate traffic is no longer blocked and that other malicious traffic is still prevented.

## Scenario 4 - Encrypted Traffic

**Your organization has implemented HTTPS across all its applications, but your IDS is failing to detect attacks within encrypted traffic. How would you address this issue?**

1. SSL/TLS Decryption:
   - Enable decryption capabilities on your IDS (or deploy a dedicated decryption proxy) to inspect HTTPS traffic.
2. Deploy an SSL/TLS Capable IDS/IPS:
   - Use an IDS/IPS system that supports encrypted traffic inspection.
3. Log Monitoring:
   - Analyze application and server logs for additional threat detection (to complement IDS).
4. Privacy Considerations:
   - Ensure compliance with privacy laws (e.g., GDPR, HIPAA) when decrypting traffic.
5. Alternative Approaches:
   - Suggest using endpoint-based detection to monitor encrypted threats directly on the host.

## Scenario 5 - Handling Zero-Day Attacks

**An attacker successfully exploited a zero-day vulnerability in your network. Your IDS had no signature for the attack, so it failed to detect it. What strategies can you implement to handle zero-day threats in the future?**

- Anomaly-Based Detection:
  - Implement anomaly-based detection methods in the IDS/IPS to monitor traffic that deviates from normal patterns.
- Threat Intelligence Integration:
  - Integrate your IDS/IPS with real-time threat intelligence feeds to identify potential zero-day attack patterns.
- Endpoint Protection:
  - Use endpoint detection and response (EDR) tools that can mitigate zero-day threats at the host level.
- Regular Patching:
  - Apply patches and updates as soon as vendors release them to close known vulnerabilities.
- Network Segmentation:
  - Isolate critical systems to minimize the spread of zero-day exploits.

## Scenario 6 - Implementing NIDS in a Large Network

**Your company is expanding, and you need to deploy a network-based IDS (NIDS) across multiple locations. What challenges might arise, and how would you address them?**

- Challenges

  - Scalability:
    - NIDS must handle large volumes of traffic without performance degradation.
  - Traffic Monitoring:
    - Deploying NIDS at critical points (e.g., behind firewalls) may result in blind spots.
  - Encrypted Traffic:
    - HTTPS traffic may not be analyzed effectively.
  - False Positives:
    - Large networks can generate numerous alerts, overwhelming security teams.

- Solutions
  - Use scalable NIDS with load balancing to distribute the monitoring workload.
  - Position NIDS strategically to monitor critical network segments.
  - Implement SSL decryption solutions for encrypted traffic inspection.
  - Tune detection rules and integrate with SIEM tools to prioritize alerts.

## Scenario 7 - SIEM and IDS Integration

**How would you integrate an IDS with a Security Information and Event Management (SIEM) system, and what benefits would this provide?**

- Integration Process:
  - Configure the IDS to forward logs and alerts to the SIEM system.
  - Use standardized formats (e.g., Syslog) for seamless integration.
- Benefits:
  - Centralized Monitoring: View IDS alerts alongside other security logs for a holistic view.
  - Correlation and Context: Use SIEM’s correlation engine to link IDS alerts with other events (e.g., firewall logs, authentication logs).
  - Improved Response: Automate responses to IDS alerts using SIEM playbooks.
  - Threat Prioritization: Filter and prioritize alerts to focus on critical threats.

## Scenario 8 - Host-Based IDS (HIDS) Deployment

**You are tasked with deploying HIDS on critical servers in your organization. What factors should you consider during deployment?**

- System Compatibility:
  - Ensure the HIDS solution is compatible with the operating systems of the servers.
- Performance Impact:
  - Evaluate the resource consumption of HIDS to avoid degrading server performance.
- Monitored Activities:
  - Decide what activities the HIDS should monitor (e.g., file integrity, process execution, privilege escalations).
- Response Mechanism:
  - Define how alerts will be handled (e.g., notify admins, trigger automated responses).
- Logging and Reporting:
  - Configure logs to integrate with SIEM or other centralized reporting tools.
- Regular Updates:
  - Keep HIDS signatures and detection models updated to stay protected against new threats.

## Scenario 9 - DDoS Attack Detection and Prevention

**Your company experiences a DDoS attack targeting its web servers. How can IDS and IPS help mitigate this attack?**

- IDS Role:
  - Detect abnormal traffic patterns (e.g., high request rates from a single IP).
  - Alert security teams about the ongoing attack.
- IPS Role:

  - Actively block malicious IPs or drop packets associated with the attack.
  - Use rate-limiting to throttle excessive traffic.

- Additional Measures:
  - Use a Web Application Firewall (WAF) to filter DDoS traffic.
  - Integrate with a DDoS protection service for large-scale attacks.
