# Network Security

## OSI Model and Protocols Overview

The **OSI (Open Systems Interconnection)** model divides network communication into 7 layers, each responsible for specific functions.

## OSI Layers and Functions

1. **Layer 7 – Application Layer**

   - Provides services for applications to communicate over the network.
   - Protocols: HTTP, FTP, SMTP, DNS, POP3, IMAP, SNMP, etc.

2. **Layer 6 – Presentation Layer**

   - Responsible for data translation, encryption, and compression.
   - Ensures that data sent by the application layer is in a readable format (e.g., encryption like SSL/TLS).

3. **Layer 5 – Session Layer**

   - Manages sessions or connections between computers.
   - Ensures that data transfer happens correctly across the session, handling start, maintenance, and termination.

4. **Layer 4 – Transport Layer**

   - Manages end-to-end communication, reliability, and flow control.
   - Protocols: TCP, UDP.

5. **Layer 3 – Network Layer**

   - Determines how data is sent between devices on the network.
   - Responsible for routing, addressing, and logical pathing.
   - Protocols: IP, ARP, ICMP.

6. **Layer 2 – Data Link Layer**

   - Handles error detection and correction and manages physical addressing.
   - Protocols: Ethernet, PPP, MAC addresses.

7. **Layer 1 – Physical Layer**
   - Defines the hardware elements like cables, switches, and physical aspects of data transmission.

## Important Protocols

1. **TCP (Transmission Control Protocol)**

   - A connection-oriented protocol used to establish a reliable communication channel.
   - Guarantees data delivery using a 3-way handshake and error-checking.

2. **UDP (User Datagram Protocol)**

   - A connectionless protocol that doesn't guarantee delivery.
   - Used for streaming or applications that need low latency (e.g., VoIP).

3. **ARP (Address Resolution Protocol)**

   - Resolves IP addresses to MAC addresses in a local network.

4. **NAT (Network Address Translation)**

   - Translates private internal IP addresses to public IP addresses and vice versa, helping with routing in IPv4.

5. **DNS (Domain Name System)**

   - Resolves domain names to IP addresses, allowing users to access websites by name instead of numeric IP addresses.

6. **DHCP (Dynamic Host Configuration Protocol)**

   - Automatically assigns IP addresses to devices on a network.

7. **SFTP (Secure File Transfer Protocol)**

   - A secure version of FTP that uses SSH to encrypt the data transfer.

8. **SNMP (Simple Network Management Protocol)**

   - Used to monitor and manage network devices like routers and switches.

9. **SMTP (Simple Mail Transfer Protocol)**

   - Protocol for sending emails between mail servers.

10. **POP3 (Post Office Protocol version 3)**

    - A protocol for retrieving emails from a mail server to a local client.

11. **IMAP (Internet Message Access Protocol)**

    - A protocol for retrieving emails from a server, allowing users to manage messages on the server itself.

12. **SCP (Secure Copy Protocol)**

    - A secure file transfer protocol that uses SSH for encrypting the data transfer.

13. **FTP (File Transfer Protocol)**

    - A standard network protocol for transferring files between systems but is unencrypted.

14. **TFTP (Trivial File Transfer Protocol)**
    - A simpler, unencrypted file transfer protocol commonly used in booting devices and transferring configuration files.

## Security in Protocols

1. **ARP Poisoning**

   - Attack where malicious ARP responses are sent to associate a victim's IP address with the attacker's MAC address, allowing for MITM attacks.

2. **DNS Cache Poisoning**

   - Malicious data is inserted into the DNS cache, redirecting users to malicious websites instead of legitimate ones.

3. **IP Spoofing**

   - An attacker sends packets with a forged IP address to trick the recipient into believing the packets come from a trusted source.

4. **MITM (Man-in-the-Middle)**

   - An attacker intercepts communication between two parties, often to steal data or inject malicious content.

5. **Ping of Death**

   - Sending malformed or oversized packets to crash or destabilize a system.

6. **SYN Flood Attack**

   - A Denial-of-Service (DoS) attack where an attacker sends a flood of SYN requests, consuming server resources and preventing legitimate connections.

7. **DNSSEC (Domain Name System Security Extensions)**

   - Provides security to DNS by ensuring the authenticity and integrity of DNS data through digital signatures.

8. **IPSec (Internet Protocol Security)**
   - A suite of protocols used to secure IP communications by encrypting data and authenticating each packet in a session.

## TCP 3-Way Handshake

The TCP 3-way handshake is used to establish a connection between a client and a server:

1. **SYN**: The client sends a SYN (synchronize) message to initiate the connection.
2. **SYN-ACK**: The server responds with a SYN-ACK message, acknowledging the client's request and sending its own synchronization signal.
3. **ACK**: The client sends an ACK (acknowledge) message, confirming the connection is established.

## IDS/IPS/IDPS

- **IDS (Intrusion Detection System)**: Monitors network traffic for signs of malicious activity and alerts administrators to potential threats.
- **IPS (Intrusion Prevention System)**: Works similarly to IDS but actively blocks detected threats.
- **IDPS (Intrusion Detection and Prevention System)**: Combines both detection and prevention, providing a proactive defense mechanism.

## HTTP Security Basics

- **GET**: Retrieves data from the server without changing any state.
- **POST**: Sends data to the server to create or update resources (e.g., submitting a form).
- **PUT**: Replaces an existing resource with the data sent.
- **DELETE**: Deletes a specified resource.

Each HTTP method has different use cases and should be used correctly to ensure the security and integrity of web applications. For example, sensitive data should not be passed using GET, as it’s exposed in URLs, and POST should be used for form submissions where data changes on the server.
