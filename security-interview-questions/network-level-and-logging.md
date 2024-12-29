# Network Level and Logging

## Common Ports Involving Security: Risks & Mitigations

### Common Ports

- Port 80 (HTTP): Risk of data interception, man-in-the-middle (MITM) attacks.
- Port 443 (HTTPS): Secure communication but still vulnerable to misconfigurations.
- Port 22 (SSH): Risk of brute-force attacks if weak passwords or misconfigurations are used.
- Port 21 (FTP): Risk of unencrypted data transfers, credential theft.
- Port 53 (DNS): Risk of DNS spoofing or cache poisoning.

#### Mitigations

- Use firewalls to block unauthorized access to these ports.
- Employ encryption (e.g., TLS/SSL) for sensitive data.
- Use strong passwords and enable multi-factor authentication (MFA) where possible.
- Regularly update software to patch vulnerabilities.

## Which port is used for DNS?

Port 53 is used for DNS (Domain Name System) communication. DNS requests typically occur over both UDP (User Datagram Protocol) for quick queries and TCP for zone transfers or when the response data exceeds 512 bytes.

## Describe HTTPS and how is it used?

HTTPS (Hypertext Transfer Protocol Secure) is an extension of HTTP that uses SSL/TLS to encrypt data between the client and the server.

HTTPS is used to securely transmit data on the web (e.g., login credentials, payment information) by encrypting the data in transit, preventing eavesdropping and tampering.

## What is the difference between HTTPS and SSL?

HTTPS is a protocol for secure communication over a network, while SSL (Secure Sockets Layer) is a cryptographic protocol that was used to provide encryption.

SSL has been replaced by TLS (Transport Layer Security), which is a more secure and efficient version.

HTTPS uses SSL/TLS to ensure secure data transmission.

## How does threat modelling work?

Threat modelling involves identifying potential security threats to a system, understand the risks associated with these therats and design mitigations.

- Identify assets, potential threats, vulnerabilities, and evaluate risks based on likelihood and impact.
- Popular methodologies include STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).

## What is a subnet and how is it useful in security?

- A subnet is a segment of an IP network that is logically separated to divide a larger network into smaller, manageable sections.
- Security Use: Subnets help limit broadcast traffic, reduce the attack surface, and isolate sensitive systems from the rest of the network, enhancing network security.

## What is a subnet mask?

A subnet mask is used to define the network portion and the host portion of an IP address. It enables routers and devices to identify which part of the IP address is used to route traffic within the same network and which part is for devices outside the network.

## What is a traceroute?

Traceroute is a network diagnostic tool used to trace the path data packets take from the source to the destination. It shows each hop (router or server) the packet goes through and measures the time it takes for each hop.

## Explain TCP/IP Concepts

TCP/IP (Transmission Control Protocol/Internet Protocol) is the foundation of internet communication. TCP ensures reliable communication (connection-oriented), while IP handles addressing and routing of data packets across networks.

## What is OSI model?

The OSI (Open Systems Interconnection) Model is a conceptual framework for understanding network communication in seven layers:

1. Physical: Transmission of raw data.
2. Data Link: Error detection and correction.
3. Network: Routing of packets (e.g., IP).
4. Transport: End-to-end communication (e.g., TCP/UDP).
5. Session: Management of sessions (e.g., opening, closing connections).
6. Presentation: Data encryption, compression.
7. Application: End-user services (e.g., HTTP, FTP).

## How does a router differ from a switch?

- Router: Directs traffic between different networks (Layer 3, IP addresses).
- Switch: Connects devices within the same network and forwards frames based on MAC addresses (Layer 2).

## How does a packet travel between two hosts connected in the same network?

In the same netowrk, a packet is sent directly to the destination host's MAC address without the need for routing (only for different network). The sender's device sends the packet with the destination MAC address obtained from the ARP table.

## Explain the difference between TCP and UDP

- TCP: Reliable, connection-oriented protocol. Ensures data integrity and guarantees packet delivery.
- UDP: Unreliable, connectionless protocol. Faster but does not guarantee packet delivery or order.

## Which is more secure, TCP or UDP?

- TCP is more secure because it establishes a connection, ensures reliable data delivery, and checks for errors.
- UDP does not offer the same reliability or error correction.

## Explain what information is added to a packet at each stop of the 7-layer OSI model

Each layer in the OSI model adds specific headers to a packet:

- Physical Layer: Bit-level data.
- Data Link Layer: Frame headers (MAC addresses).
- Network Layer: IP header (IP addresses).
- Transport Layer: TCP/UDP header (port numbers).
- Session Layer: Session data.
- Presentation Layer: Encryption or data transformation.
- Application Layer: Data relevant to the application (HTTP, FTP).
