# Information Security Interview Preparation (Intrusion Detection and Prevention System)

## Intrusion Detection System (IDS)

- System designed to monitor and analyse network traffic for signs of security breaches, malicious activities, or policy violations.
- Does not block traffic (this is firewall)
- Passive
- Deployed parallel to network traffic, analyses a copy of the traffic and does not directly interact with it
- e.g SIEM system

## Types of Intrusion Detection System (IDS)

### Network-based IDS (NIDS)

- Monitors traffic on a network
- Deployed at critical points (routers, firewalls)
- Use Case
  - Detect abnormal traffic patterns
  - DoS attacks
  - Protocol misuse

### Host-based IDS (HIDS)

- Monitors activity on a specific host/device
- Tracks system logs, file changes and process activity
- Use Case
  - Detect file integrity issues
  - Unauthorised changes
  - Privilege escalations

### Hybrid IDS

- Combines the strengths of both network-based and host-based IDS
- Example
  - Security Information and Event Management (SIEM) like Splunk

## Intrusion Prevention System (IPS)

- Active system that monitor, analyses and blocks malicious traffics in real-time.
- Basically IDS + ability to block malicious traffics
- Active
- Additional layer behind firewall, deployed directly in the path of network traffic
- E.g Inline firewalls with IPS functionality

## Types of Intrusion Prevention System (IPS)

### Network-based IPS (NIPS)

- Monitors traffic on a network
- Positioned behind firewalls
- Use Case
  - Detects and blocks exploits such as DDoS, worms, or unauthorised attempts

### Host-based IPS (HIPS)

- Installed directly on individual host (server) to monitor and protect them
- Monitor application behaviour and protect against any malware by blocking them

## Detection Methods

### Signatured-based Detection

- Uses pre-defined patterns of known attacks
- Effective for known threats but weak against zero-day attacks (never seen before)

### Anomaly-based Detection

- Monitor whether traffics deviate from the normal behaviour
- Effective for unknown threats, but prone to false positives

### Hybrid Detection

- Combines both signature-based and anomaly-based methods
- Balances accuracy and ability to detect unknown threats

## Key Components of IDS

1. Traffic Monitoring
   - Network-based IDS analyses packets at the network level.
   - Host-based IDS examines system logs, file systems and process activity.
2. Detection Engine
   - Applies detection rules (signature - pre-defined) or models (anonmaly detection) to identify threats.
3. Alerting System
   - Sends notification or logs suspicious activity
   - Integrate with SIEM tools for correlation and reporting
4. Response Mechanism
   - IDS is passive and does not block threats, it only monitors behaviours.
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
