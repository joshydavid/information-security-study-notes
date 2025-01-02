# Commonly Asked Interview Questions

## Explain the differences between TCP and UDP protocols, and when would you choose one over the other?

TCP (Transmission Control Protocol) is a connection-oriented protocol that ensures reliable and ordered delivery of data. UDP (User Datagram Protocol), on the other hand is a connectionless protocol that priorizes speed and efficiency. TCP is suitable for applications requiring data delivery such as web browsing (HTTPS) while UDP is preferred for real-time applications such as live streaming or online gaming.

## Describe the process of subnetting and its significance in network design

Subnetting involves dividing a larger network into smaller sub-networks. It enhances network performance, minimises broadcast traffic, and optimise IP address allocation. By assigning unique subnets to different departments or funcitons, it promotes organisation and efficient use of IP addresses.

## How does DNS work and what role does it play in internet communication?

DNS translates human readable domain names into machine readable IP addresses to facilitate communication on the internet. DNS acts as a phonebook of the internet so humans don't have to remember and memorise IP addresses.

## Discuss the concept of VLANs (Virtual Local Area Networks) and their applications in network architecture

They are virtual segments within a physical network, enabling logical isolation of devices regardless of their physical location. It enhances network security, simplify network management and improve overall efficiency by grouping devices with similar requirements.

## Explain the purpose of ARP in a local network

ARP resolves IP addresses to MAC addresses in a local network. When a device needs to communicate with another device on the same network, ARP is used to obtain the corresponding MAC address. (Layer 2 - Data Link)

## Describe the role of NAT and how does it impact IP address allocation?

NAT translate private IP addresses to a single public IP address, allowing multiple devices in a private network to share a common public IP when accessing the internet. It's essential to conserve public IP addresses and enhance network security by concealing internal IP structures.

## Discuss the security implications of implementing wireless networks, and how would you secure a wireless network effectively?

Wireless network security involves encryption, authentication mechanisms and access controls to prevent unauthorized access and protect data transmission. Implementing WPA3 encryption, strong authentication protocols, and regular security audits are crucial for securing wireless networks.

## Explain the concept of VPN and its applications in remote access and secure communications

VPNs establish secure, encrypted connections over the internet, providing a private network experience for remote users. They ensure confidentiality, and integrity of data during transmission, making them essential for secure remote access and interconnecting geographically distrubuted networks.

## What is the role of firewalls in network security, and how do stateful and stateless firewalls differ?

Firewalls monitor and control incoming and outgoing network traffic. Stateful firewalls track the state of active connections, making decisions based on the context of traffic.

Stateless firewalls filter traffic based on **predefined security rules** without considering the connection state.
IPS - deep packet inspection to identify known attack signatures / anamolous patterns that firewalls won't catch. Firewalls do basic filtering based on headers (IP addresses, ports, protocol)
