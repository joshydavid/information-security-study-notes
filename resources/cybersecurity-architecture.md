# Cybersecurity Architecture

## Five Principles to Follow

### ✅ Defense in Depth

- Create an obstacles for the attackers. Not relying on single security mechanism to keep the security safe.
- Castle: good guys on the inside, bad guys on the outside. Door is a vulnerability, need to reinforce it.
- Modern security: User -> web server -> app server -> database
  - User: MFA - who they say they are. something they know, something they have, something they are.
  - EDR: next generation anti-virus to make sure the platform is secure.
  - Network: Firewall, IDPS
  - Web/app server: Vulnerability testing, data is encrypted, access control in-place.
- No single point of failure, if one fails - the rest still works. Fails safe too.

### ✅ Principle of Least Privilege

- Grant minimum level of access rights to those who are authorised to perform their jobs.
- Hardening a system: HTTP, FTP, SSH server. Do you really need the FTP? else remove. Do you really need SSH? else remove. Every single open port is making us vulnerable. Remove unnecessary services.
- Eliminate privilege Creep: "Just in case" if you need it <- this is the opposite of principle of least privilege.

### ✅ Separation of Duties

- No single point of control
  - Physical world: user A wants access to the database, requires approval. Requestor != Approval

### ✅ Security By Design

Security should not be an afterthought. Include security at the start of development.

- Secure coding
- Secure system
- Secure test data
- Secure production system/data

Designer, developer, adminstrator, user everyone is responsible.

### ✅ Keep It Simple, Stupid (KISS)

- Don't make it harder than necessary, easy for attackers, harder for good guys.
- Make the system secure, but also make it simple.

### ❌ Security By Obscurity

- Secret != Secure
- We want a system that is open, only the key should be kept secret. The algorithms should be made known.
- The key is the only secret.

## Frameworks

### Incident Response Lifecycle (NIST 800-61)

- Preparation and Prevention
- Detection and Analysis
- Containment
- Eradication
- Recovery
- Post-Mortem

## Endpoints Management

### What are they?

- It's an entry point for cyberattacks
- Endpoints: devices that are connected to network
- Hardware perspectives: Server, IOT, MacBook Pro, iPhone 16, router, switches
- Software perspectives: iOS 18, macOS Sequoia

### Controls

- Inventory: Query which hardware? Which software is present?
- Security Policy: What types of devices are allowed in the organisations? Software release, current release, current release - 1? Password policy, expiry in XX days
- Patching: Old software, security fixes
- Encryption: Data should all be encrypted
- Remote Wipe: In case the device gets stolen, we can do a remote wipe of all the data
- Location Tracking: In case something is missing
- Anti-virus / Endpoint Detection Response: No malware
- Disposal: How/where to throw such that our information is not exposed?

### Bring Your Own Device (BYOD)

- Well-defined, poorly defined program.
- Consent: Allow monitoring, usage, wiping
- Software: Which software version?
- Hardware: Support only Apple devices, no Android devices.
- Services: Authentication

## Network Security

### Firewalls

Fire in real life: Limit the fire from spreading, it may not go away completely. Isolate from danger.

**Packet Filter**
Network: internet facing > firewall here > internal network.
Look into the packet (source address, destination address, port number) and block it if its malicious

Header contains the `source, destination, port`. Looks at a closed envelope.

**Stateful Packet Inspection**

Looks at the payload as well, not just the header. Open the envelope and look at the content inside.

**Proxy**

- Something that acts on behalf of something else.
- Browser -> proxy server -> actual server
- Good "man-in-the-middle"

**Network Address Translation**

- Internal address that cannot be routed to the internet
- Translate private addresses to public addresses
- Translate 192.168.1.1 to an external address so that it can reach the internet

### VPN

- Secure channel over untrusted network
- Encrypted information and sent over the network
- "Secure pipe" nothing can be interpreted, all encrypted
- Limited inspection capability, a bad guy could send a traffic in.

## Application Security

- All softwares have bugs
- % of those bugs will have security vulnerabilities
- All softwares will ahve security vulnerabilities

### Secure Coding

- Coding practices/checklist such as validate inputs to prevent SQL injections
- OWASP top 10
- Trusted libraries (Log4j vulnerability)
- Standard architectures
- Mistakes to avoid (owasp top 10 vulnerabilities)
- SBOM, like a supply chain
  - Components
  - Libraries
  - Dependencies
  - Versions

## Vulnerability Testing

- SAST

  - whitebox
  - Scans source code like SonarQube, Dependabot
  - Finds vulnerabilities earlier

- DAST
  - "black" box
  - Obsourced source code, looks at the executable systems - after the coding phase
  - Finds vulnerabilities later

Not an either or, but both.

## Detection

Security = Prevention + **Detection** + Response
The topics above are all about prevention.

CIA - What?
S = P + D + R - How?

**SIEM - Security Information Event Management**

Primarily a log management and event correlation tool that helps with incident detection, investigation, and compliance. It’s best for organizations that need to collect and store large volumes of logs, analyze historical data, and meet compliance requirements.

### Monitor

- Consistent single view of everything that is happening
- Aggregate logs/alarms/events from all the different system and feed it to a higher system known as SIEM.
- See it as a single alarm.

### Analyse

- Look at rules, policies, anamolies, trends
- Location, login too many times, failed logins etc.

### Report

- Reports all the data collected

### Threat Hunting

- Recon
- Mean time to identify (MTTI) ~200 days
- Mean time to contain ((MTTC)) ~70 days

Ideally, be aware of the attack. If I can't prevent the attack, at least be aware of it sooner - via threat hunting.

Reactive: System notified (alert) -> forensic investigation
Proactive: Threat hunting. No alarms yet, get ahead before the attacker even strikes.

**XDR - Extended Detection and Response**

A more integrated, proactive solution that focuses on real-time detection, automated response, and threat hunting across various layers of the IT environment (endpoint, network, cloud). It is designed to provide comprehensive threat detection and reduce the need for manual intervention.

Federated search - look for indicators of compromise, run a search locally and report result only if it's malicious. SIEM good for alarms - ALL information is coming up. XDR fetch just in time.

`not (SIEM vs XDR)`
`SIEM + XDR`

## Response

- Security = Prevention + Detection + **Response**
- Mean Time to Contain - Response
- Can we shrink 70 days to shorter?

### SOAR - Security Orchestration Automation and Response

- Traditionally it is a manual process, but the modern approach is to automate it.
- SIEM -> feeds to XDR -> CASE
  - Opens up the case in the SOAR system
  - Use SOAR to modify/assign cases
  - SIEM + XDR contain useful information, indicators of compromise so that the cyybersecurity analysts can use them

## TLDR

1. `SIEM` detects unusual activity from an endpoint based on log data and generates an alert.
2. `XDR` analyzes the activity more deeply, correlating data from the endpoint with network traffic and email security logs, and confirms that the activity is malicious (e.g., ransomware).
3. `SOAR` triggers an automated response to isolate the compromised endpoint, block any associated IP addresses, and send a notification to the security team. It also triggers a workflow for analysts to investigate further and document the incident.
