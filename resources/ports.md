# Ports

## Networking Protocols

### FTP (File Transfer Protocol)

Port `20` - Data transfer
Port `21` - Command/control

### SSH (Secure Shell)

Port `22` - Used for secure remote access, file transfers and tunneling

### Telnet

Port `23` - Unencrypted remote access that is insecure, avoid in favor of SSH.

### SMTP (Simple Mail Transfer Protocol)

Port `25` - Used for sending emails. Use port `587` or `465` for encrypted SMTP.

### DNS (Domain Name System)

Port `53` - Resolves domain name to IP addresses. UDP for queries, TCP for zone transfers.

### DHCP (Dynamic Host Configuration Protocol)

Port `67` - Server to client
Port `68` - Client to server

### TFTP (Trivial File Transfer Protocl)

Port `68` - Simplified version of FTYP, typically used for transferring small files.

### HTTP (Hypertext Transfer Protocol)

Port `80` - Standard web traffic over the internet.

### HTTPS (HTTP Secure)

Port `443` - Encrypted web traffic using SSL/TLS

## Security and Monitoring

### IPSec

Used for VPNs and encrypted communications.

Port `50` - ESP (Encapsulating Security Payload)
Port `51` - AH (Authentication Header)

### SNMP (Simple Network Management Protocol)

Port `161` - Agent queries
Port `162` - SNMP traps (alerts from devices)

### Syslogs

Port `514` - Logging network events and security data

### OpenVPN

Port `1194` - VPN service

### RDP (Remote Desktop Protocol)

Port `3389` - Used for remote desktop connections to Windows systems.

## Database Services

### Microsoft SQL Server

Port `1433` - Database server traffic

### Oracle Database

Port `1521` - Oracle database connections

### MySQL

Port `3306` - Default MySQL database traffic

### PostgreSQL

Port `5432` - PostgreSQL database traffic

## Email Services

### POP3 (Post Office Protocol v3)

Port `110` - Retrieves emails from a server. Use port 995 for encrypted POP3.

### IMAP (Internet Message Access Protocol)

Port `143` - Access emails on a server. Use port `993` for encrypted IMAP.

## File Sharing and Directory Services

### NFS (Network File System)

Port `2049` - Used for sharing files over the network.

## Miscellaneous

### NTP (Network Time Protocol)

Port `123` - Synchronizes system clocks.

### IRC (Internet Relay Chat)

Port `6667` - Often used in botnet command-and-control communications.

### Alternative HTTP

Port `8080` - Commonly used for web servers or proxies.
