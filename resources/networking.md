# Information Security Interview Preparation (Networking Fundamentals)

## What is Networking?

Networks are simply things connected, it can found in all walks of life such as meeting new people. In computing, networking is the same idea, network is formed by anywhere from 2 devices to billions.

## What is the Internet?

The internet is a giant network that consists of many small networks within itself, it allows devices and servers to communicate and share information through set of standardised protocols known as Internet Protocol (IP)

![Internet](./images/networking/internet.png)

## Identifying Devices on a Network

Humans

- Name (mutable, name changed)
- Fingerprint (immutable)

Device

- IP Address (mutable)
- MAC Address (Media Access Control, immutable)

### IP Address

- Identify a host on a network
- Made up of 4 octets, betwee the range of 0 and 255 (inclusive)
- Mutable
- Public address -> identify devices on the internet
- Private address -> identify devices amongst other devices

IPv4

- 2^32 IP address (~4.29 billions)
- Router address (Wifi A - same)
  - iPhone private IP address (different)
  - MacBook Pro private IP address (different)
- Running out of IP address as more devices are connected to the internet

IPv6

- Newer iteration, up to 2^128 IP address (~340 trillion)
- Solves the limitation of IPv4

![IP Address](./images/networking/ip_address.png)

### MAC Address

- Found in device's motherboard
- Assigned a unique address at the factory (MAC)
- 12 character hexadecimal number
- First 6 digit represents the company, last 6 represents a unique number
- Can be spoofed - ARP poisoning
- Networked device pretends to identify as another using its MAC address

## Ping

- Uses ICMP (Internet Control Message Protocol) packets to determine the performance of a connection between device
- `ping <IP address or website URL>`

## TCP

[TCP](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)

### Three-way Handshake (Establish Connection - Layer 4)

![3 Way Handshake](./images/networking/tcp_handshake.png)

- SYN Packet: The source sends an SYN packet to the target server to initiate the connection.
- SYN-ACK Packet: The target server responds with a SYN-ACK packet to acknowledge the connection request.
- ACK Packet: The source sends an ACK packet to confirm the connection, completing the 3-way handshake.
- Data Transfer: The email message is broken down into smaller packets for transmission.
- Routing: Packets traverse multiple gateways across the internet.
- Reassembly: Upon reaching the target device, TCP reassembles the packets into the original email content.

### Advantage

- Ensures reliable data delivery by providing acknowledgements
- Data arrives in order
- Flow control
- Use case
  - Web browsing
  - Email
  - Remote access (SSH)

TLDR, speed > reliability - UDP, otherwise TCP.

- UDP use case
  - DNS queries
  - Online gaming
  - Livestream

## OSI Model (Open Systems Interconnection)

- The OSI model breaks down network communication into 7 distinct layers
- Purpose: understand how different networking protocols interact with each other and how data flows across a network
- Each layer handles communication and job with the layer above and below itself.

![OSI Model](./images/networking/osi_model.png)

### Layer 7 - The Application Layer

![Layer 7](./images/networking/layer_7.png)

- Only layer that directly interacts with data from the user
- Helps to initate communication via protocols such as HTTP and SMTP

### Layer 6 - The Presentation Layer

![Layer 6](./images/networking/layer_6.png)

- Prepare data to be used by the application layer
- Layer 6 makes the data presentation for application to consume
- Responsible for translation, encryption, compression of data
- For encryption, layer 6 will encrypt on sender end and decrypt on receiver end so that it can present the application layer with unencrypted, readable data
- Compresses data it receives from layer 7 before delivering it to layer 5 to improve speed and efficiency

### Layer 5 - The Session Layer

![Layer 5](./images/networking/layer_5.png)

- Responsible for opening/closing communication between 2 devices known as session
- Stay open long enough to transfer all the data, but promptly closes to avoid wasting resources

### Layer 4 - The Transport Layer

![Layer 4](./images/networking/layer_4.png)

- Responsible for end-to-end communication between 2 devices
- Take data from session layer and break up into chunks called segments before sending to layer 3.
- Receiving device is responsible for reassembling the segments into the data the session layer can consume
- Responsible for flow control and error control
- Determines optimal speed of transmission to ensure that sender with fast connection does not overwhelm receiver with slow connection
- Error control on receiving end by ensuring that data received is complete and request a retransmission if it isn't
- Communication stops here if you are developing a full-stack application on the same machine.
- Protocols - TCP, UDP

### Layer 3 - The Network Layer

![Layer 3](./images/networking/layer_3.png)

- Responsible for facilitating data transfer between 2 different networks
- If both devices communicate on the same network (localhost and localhost), this layer is not needed.
- Breaks up segments from the transport layer into small units called packets on the sender's device
- Reassemble these packets on the receiving device
- Finds the best physical path for the data to reach its destination known as Routing
- Protocols - IP, ICMP, IGMP, IPsec

### Layer 2 - The Data Link Layer

![Layer 2](./images/networking/layer_2.png)

- Similar to network layer except this facilitates data transfer between 2 devices on the same network.
- Takes packets from the network layer and breaks them into smaller pieces called frames.
- Responsible for flow control and error control for intra-network communication.

### Layer 1 - The Physical Layer

![Layer 1](./images/networking/layer_1.png)

- Involves physical equipment involved in data transfer such as cables and switches
- Data gets converted into bit stream, (0s and 1s)
- The physical layer of both devices must also agree on a signal convention so that 1s can be distinguished from the 0s on both devices.

### How data flows through the OSI Model

In order for human-readable information to be transferred over a network from one device to another, the data must travel down the seven layers of the OSI Model on the sending device and then travel up the seven layers on the receiving end.

For example: Mr. Cooper wants to send Ms. Palmer an email. Mr. Cooper composes his message in an email application on his laptop and then hits ‘send’. His email application will pass his email message over to the application layer, which will pick a protocol (SMTP) and pass the data along to the presentation layer. The presentation layer will then compress the data and then it will hit the session layer, which will initialize the communication session.

The data will then hit the sender’s transportation layer where it will be segmented, then those segments will be broken up into packets at the network layer, which will be broken down even further into frames at the data link layer. The data link layer will then deliver those frames to the physical layer, which will convert the data into a bitstream of 1s and 0s and send it through a physical medium, such as a cable.

Once Ms. Palmer’s computer receives the bit stream through a physical medium (such as her wifi), the data will flow through the same series of layers on her device, but in the opposite order. First the physical layer will convert the bitstream from 1s and 0s into frames that get passed to the data link layer. The data link layer will then reassemble the frames into packets for the network layer. The network layer will then make segments out of the packets for the transport layer, which will reassemble the segments into one piece of data.

The data will then flow into the receiver's session layer, which will pass the data along to the presentation layer and then end the communication session. The presentation layer will then remove the compression and pass the raw data up to the application layer. The application layer will then feed the human-readable data along to Ms. Palmer’s email software, which will allow her to read Mr. Cooper’s email on her laptop screen.

### Data Flow

Sender: Layer 7 -> Layer 1

1. Application: Application creates data (e.g., sending an email).
2. Presentation: Data is formatted, encrypted, or compressed.
3. Session: The session between the sender and receiver is initiated.
4. Transport: Data is segmented into smaller packets, and error-checking is performed (e.g., TCP ensures reliability).
5. Network: The data packet is routed based on IP addresses.
6. Data Link: The data packet is framed with physical addresses (MAC address) for local delivery.
7. Physical: The data is transmitted as electrical signals or light pulses.

Receiver: Layer 1 -> Layer 7

1. Physical: Signals are received and converted into bits.
2. Data Link: Data is extracted from the physical frames.
3. Network: Data is routed to the correct destination.
4. Transport: Segments are reassembled, and error correction is applied.
5. Session: The session is maintained.
6. Presentation: Data is decrypted and decompressed, if necessary.
7. Application: Data is presented to the user or application.

### Information Security Context

#### Layer 7: Application Layer

- Security Focus: This layer deals with user-facing applications and network services.
- Risks: Vulnerabilities like SQL injection, Cross-Site Scripting (XSS), and buffer overflows can be exploited here.
- Security Measures:
  - Implement input validation to prevent injection attacks.
  - Use encryption for sensitive data in transit.
  - Web Application Firewalls (WAFs) can help protect web apps.

#### Layer 6: Presentation Layer

- Security Focus: This layer is responsible for data formatting, encryption, and compression.
- Risks: Poor encryption practices or misconfigured settings can expose sensitive data.
- Security Measures:
  - Use strong end-to-end encryption (e.g., TLS/SSL for secure communications).
  - Ensure proper handling of data compression and decompression to avoid vulnerabilities.

#### Layer 5: Session Layer

- Security Focus: The session layer establishes, maintains, and terminates communication sessions.
- Risks: Man-in-the-middle (MITM) attacks, session hijacking, or replay attacks can occur here.
- Security Measures:
  - Use session tokens and implement multi-factor authentication (MFA).
  - Utilize session timeouts to minimize the risk of unauthorized access after inactivity.

#### Layer 4: Transport Layer

- Security Focus: Manages end-to-end communication, including error recovery and flow control.
- Risks: Attackers can target transport protocols (e.g., TCP/UDP) to disrupt services or intercept data.
- Security Measures:
  - Use TLS/SSL to secure data transmitted via protocols like HTTP (HTTPS).
  - IPsec can secure VPN connections.
  - Firewalls and Intrusion Detection Systems (IDS) help prevent unauthorized traffic.

#### Layer 3: Network Layer

- Security Focus: Manages the routing of data across different networks using IP addresses.
- Risks: IP spoofing, routing attacks, and DDoS attacks (Distributed Denial of Service) are common here.
- Security Measures:
  - Implement firewalls to control incoming/outgoing traffic.
  - Use IPsec or VPNs for secure communications over untrusted networks.
  - Network Address Translation (NAT) can help obfuscate internal IP addresses.
  - Routers should have anti-spoofing mechanisms.

#### Layer 2: Data Link Layer

- Security Focus: Provides reliable data transfer over a single link, using MAC addresses.
- Risks: Attacks like MAC spoofing, ARP poisoning, and VLAN hopping can compromise the integrity of the data link.
- Security Measures:
  - Use MAC address filtering to restrict access to trusted devices.
  - Implement 802.1X for port-based network access control.
  - Use VLAN segmentation and secure VLAN configurations to prevent unauthorized access.

#### Layer 1: Physical Layer

- Security Focus: Involves the physical transmission of data over the network medium (e.g., cables, wireless).
- Risks: Physical attacks, such as cable tapping, unauthorized access to hardware, or denial of service (DoS) attacks via physical disruption.
- Security Measures:
  - Implement physical security for network hardware (e.g., access control to data centers).
  - Use fiber optics for secure communication, as they are harder to tap.
  - Wireless networks should use strong WPA2 or WPA3 encryption.

### Firewall

- Network security that monitors and control incoming/outgoing traffic based on pre-defined security rule.
- Purpose
  - Block unauthorised access and ensure that only legit traffic can go through

### What is a DNS?

DNS stands for Domain Name System, it is a system that translate human-readable domain name such as Apple.com into machine-readable IP address such as 192.168.1.1

DNS is like a phonebook of the internet so that we don't have to remember the complex IP address.

When you type a URL into your browser, the DNS first checks if the IP address is already stored in a local DNS cache (on your device, browser, or router). If the IP address is in the cache, the DNS system will use the cached address, which speeds up the process. If the IP address is not cached, the DNS will perform a DNS query to resolve the domain name by looking up the IP address. Once the correct IP address is found, it’s mapped to the domain name, and the browser can then connect to the correct server.

### How does the internet work?

- The internet is a global network that uses protocols like TCP to communicate.
- When a device connects to the internet, it uses an IP address to identify itself.
- Data is transferred in packets over a series of routers, switches, and networks, ensuring communication between devices.
- Protocols like HTTP, DNS, and SMTP ensure specific functions like web browsing, domain name resolution, and email exchange.

### What happens when you visit Apple.com in the browser?

- Enter Apple.com into the browser
- Translate the URL (Apple.com) into an IP address
- The mapping is stored in a cache, and the browser look for the IP address in multiple layers of cache (browser, OS, local, ISP)
- If the IP address is not found, the browser will request the DNS resolver to resolve it
- The DNS resolver performs a recursive DNS look up until it is found
- Once the IP address is found, the browser sends a HTTP request to the server hosting Apple.com using TCP/IP protocol
- We should always use HTTPS for secure access.
- The browser initiates a TCP connection with the server via TCP 3-way handshake. (Establish the Communication)
- After the TCP connection is established, SSL/TLS takes over to secure the communication. This process ensures that data transmitted between the browser and server is encrypted and secure.
- The server sends its public key to the client, the client uses the public key to encrypt the session key and sends to the server.
- The server uses its private key to decrypt the session key.
- The secure channel is established, and now it can exchange encrypted data using the session key.
- The server processes the request and responds with the page's HTML, CSS, JavaScript and other static assets.
- The browser then processes the files and renders the page to the frontend.

### What happens when you do a search on Google?

- Enter Apple internship as part of the search query
- The browser resolves the IP address for Google's search service via DNS and establish a connection via HTTPS
- The search query, alongside metadata is sent to Google's server
- Google's algorithm will parse the query and identify keywords, retrieves relevant indexed webpages from its database and rank them based on factors like relevance, page quality, user location, and past behavior.
- Google then sends the ranked list of search results to the browser
- The browser then renders the result, and we can click on the links to further explore
