# Cryptography

## Encryption, Encoding, Hashing, Tokenization, Masking

1. **Encryption**: The process of converting plaintext into unreadable data using a cryptographic algorithm, ensuring data confidentiality.
2. **Encoding**: The process of converting data into a different format to ensure safe transmission or storage, not primarily for security.
3. **Hashing**: The process of generating a fixed-length output (hash) from variable-length input, typically used for integrity checks.
4. **Tokenization**: The process of replacing sensitive data with a unique identifier (token) that holds no meaningful value outside of the system.
5. **Masking**: The process of obscuring part of the data to protect sensitive information (e.g., showing only the last four digits of a credit card number).

## Encryption

### Block vs Stream Ciphers

- **Block Ciphers**: Encrypts data in fixed-size blocks (e.g., AES). It’s efficient for encrypting large amounts of data.
- **Stream Ciphers**: Encrypts data bit by bit or byte by byte (e.g., RC4). It is suitable for data streams or when the full data length is not known.

### Symmetric Ciphers

- **AES (Advanced Encryption Standard)**: A widely used symmetric key encryption algorithm, considered very secure.
- **DES (Data Encryption Standard)**: An older encryption standard now considered insecure due to short key length.
- **3DES (Triple DES)**: An enhancement of DES, applying the DES algorithm three times for better security.

### Asymmetric Ciphers

- **RSA**: A public-key encryption algorithm widely used for secure data transmission.
- **Diffie-Hellman**: A method for securely exchanging cryptographic keys over a public channel.

### Modes of Encryption

- **CBC (Cipher Block Chaining)**: A block cipher mode where each plaintext block is XORed with the previous ciphertext block before encryption.
- **ECB (Electronic Codebook)**: A simple block cipher mode where each block is encrypted independently. Less secure due to pattern repetition in ciphertext.
- **OFB (Output Feedback)**: A mode that uses previous ciphertext for encryption, turning a block cipher into a stream cipher.
- **CFB (Cipher Feedback)**: Similar to OFB but uses feedback in a different way, making it more secure than ECB.

  **Which is Safer?**

  - **CBC** is safer than **ECB**, as it prevents ciphertext patterns and improves security.

### AEAD (Authenticated Encryption with Associated Data)

- Provides both confidentiality (encryption) and integrity (authenticity). AEAD algorithms ensure that data hasn't been tampered with during transmission.

### GCM (Galois/Counter Mode)

- A mode of encryption that combines counter mode encryption with Galois authentication, providing both confidentiality and integrity.

### Padding and IV (Initialization Vector)

- **Padding**: Extra data added to plaintext to make its length compatible with the block size.
- **IV**: A random value added to ensure the ciphertext is unique, even if the same plaintext is encrypted multiple times.

## Attacks

1. **Known Plain-text Attack**: The attacker has both the plaintext and its corresponding ciphertext and uses this information to deduce the encryption key.
2. **Chosen Plain-text Attack**: The attacker can choose plaintexts and obtain their ciphertexts, helping to reverse-engineer the encryption.
3. **Known Ciphertext-only Attack**: The attacker has ciphertext and attempts to deduce the plaintext or the key.
4. **Chosen Ciphertext-only Attack**: The attacker can select ciphertexts and learn about the plaintext, which may allow key recovery.
5. **Side Channel Attacks**: Attacks that exploit physical leaks during the encryption process (e.g., timing or power consumption).
6. **Replay Attacks**: The attacker intercepts and retransmits valid messages to deceive the system.

## Confusion and Diffusion (Avalanche Effect)

- **Confusion**: Ensures that the relationship between plaintext and ciphertext is complex and non-linear.
- **Diffusion**: Ensures that the plaintext’s bits are spread across the ciphertext, making patterns harder to detect.
- **Avalanche Effect**: A small change in the input should drastically change the output, ensuring strong confusion and diffusion.

## Hashing

### SHA-1/2/3

- **SHA-1**: A cryptographic hash function that has been deemed insecure due to vulnerabilities.
- **SHA-2**: A family of hash functions (SHA-224, SHA-256, SHA-384, SHA-512) used widely for secure hashing.
- **SHA-3**: The latest member of the SHA family, built with a different structure from SHA-2 for enhanced security.

### MD5 - Why is it not secure?

- **MD5** is vulnerable to collision attacks, where two different inputs produce the same hash. It's considered broken and unsuitable for cryptographic purposes.

### When to use hashing vs. encryption

- **Hashing**: Used for integrity checking, such as verifying passwords.
- **Encryption**: Used for data confidentiality, such as encrypting sensitive files.

### Rainbow Tables

- Precomputed tables used for reversing cryptographic hash functions. They make brute-forcing password hashes easier by storing hash values.

### Salting

- Adding a random value (salt) to input data before hashing to ensure that identical data produces different hashes.

## Hashing Attacks

1. **Collision Attack**:

   - **One-way**: Finding two distinct messages that result in the same hash.
   - **Two-way**: Finding a message that hashes to a specific target value.

2. **Pre-image Attack**:
   - Finding a message that produces a specific hash value.

## Digital Signature

### MAC (Message Authentication Code)

- A short piece of data used to verify the integrity and authenticity of a message.

### MAC vs HMAC

- **MAC**: Typically uses a secret key for creating the authentication code.
- **HMAC**: A more secure form of MAC that uses a cryptographic hash function along with a secret key.

### HMAC-SHA

- HMAC using the SHA family of hash functions (SHA-1, SHA-2, etc.).

### Signing and Verification

- **Signing**: The sender signs the message with their private key to ensure authenticity.
- **Verification**: The recipient verifies the message using the sender’s public key to ensure it hasn’t been tampered with.

## DSA and ECDSA

- **DSA (Digital Signature Algorithm)**: A standard for creating digital signatures.
- **ECDSA (Elliptic Curve Digital Signature Algorithm)**: A variant of DSA using elliptic curve cryptography for better efficiency and security.

## Tokenization

### What is it?

- **Tokenization**: The process of replacing sensitive data with tokens that have no meaningful value outside of the system.

### FPE (Format-Preserving Encryption) and SST (Substitution-based Tokenization)

- **FPE**: Encrypts data while preserving its original format.
- **SST**: Replaces sensitive data with a token that retains the original format and length.

### Is it different from masking?

- **Masking**: Hides part of data (e.g., showing only the last four digits of a credit card), while tokenization replaces it entirely.

## SSH Key-Pair

- A pair of cryptographic keys (public and private) used for authentication in secure shell (SSH) connections.

## PGP - Keyring

- **PGP (Pretty Good Privacy)**: A cryptographic tool for securing email and files, using a keyring to store public and private keys.

## PBKDF2 (Password-Based Key Derivation Function 2)

- A key derivation function designed to enhance password security by applying multiple iterations of a cryptographic hash function.

## PKI (Public Key Infrastructure)

Public Key Infrastructure (PKI) is a framework that manages digital keys and certificates to enable secure communication and authentication over a network. PKI uses asymmetric cryptography (public and private key pairs) to ensure the confidentiality, integrity, authenticity, and non-repudiation of data exchanged between entities.

## Digital Certificate

### What is it and what is it used for?

A **digital certificate** is a cryptographic document used to verify the identity of an entity (person, organization, or device) and establish secure communication via encryption. It ensures that the public key contained within the certificate belongs to the entity it claims to represent.

### Formats

- **.pem**: Privacy-Enhanced Mail, a Base64 encoded format often used for certificates and private keys.
- **.crt**: Certificate file, commonly used to store certificates.
- **.cer**: Certificate file, can be used interchangeably with .crt, often in binary or Base64 encoded format.
- **.key**: Private key file, used for signing or decrypting data.
- **.der**: Distinguished Encoding Rules, a binary format for encoding certificates and private keys.

### Various Fields/Components Inside a Certificate

- **Subject**: Identifies the entity the certificate represents.
- **Issuer**: The CA (Certificate Authority) that issued the certificate.
- **Validity Period**: The start and end dates during which the certificate is valid.
- **Public Key**: The public key used for encryption or signature verification.
- **Signature Algorithm**: The algorithm used to sign the certificate (e.g., RSA, ECDSA).
- **Serial Number**: A unique identifier assigned by the CA.

### Certificate Generation Process

1. **Generate Key Pair**: Create a public-private key pair (public key for encryption, private key for signing).
2. **Store Private Key**: The private key is stored securely, often on a hardware security module (HSM).
3. **Create CSR (Certificate Signing Request)**: Combine the public key with the entity's identity and generate a CSR.
4. **CA Signs with its Private Key**: The Certificate Authority (CA) signs the CSR with its private key.
5. **Verify with CA's Public Key**: The CA's public key is used to verify the authenticity of the certificate.

### CA, RA, VA

- **CA (Certificate Authority)**: The entity that issues and signs digital certificates.
- **RA (Registration Authority)**: A part of the CA responsible for accepting requests for digital certificates.
- **VA (Validation Authority)**: Verifies the validity of certificates.

### Key Exchange and Distribution

- The public key is exchanged between parties, while the private key is kept secure and never shared.

### Difference Between Server and Client Certificates

- **Server Certificate**: Used to authenticate the server to the client.
- **Client Certificate**: Used to authenticate the client to the server.

### Different CAs and Models

- **Single-tier**: Only the Root CA acts as the issuing CA.
- **Two-tier**: The Root CA is offline, and the Issuing CA signs certificates.
- **Three-tier**: The Root CA, Intermediate CA, and Issuing CA form a chain.

### Chain of Custody/Chain of Trust

- The **client certificate** trusts the **issuing CA**, the **issuing CA** trusts the **intermediate CA**, and the **intermediate CA** trusts the **root CA**.
- The **Root CA’s certificate** is self-signed using its own private key.

### Key Used to Sign the CA’s Certificate

- **Root CA** uses its **private key** to sign its own certificate.
- If it is an **intermediate/issuing CA**, it is signed using the **root CA's private key**.

## S/MIME (Secure/Multipurpose Internet Mail Extension)

S/MIME is a standard for public key encryption and signing of MIME data, which is commonly used for securing emails. It ensures confidentiality, integrity, and authenticity in email communication by encrypting email content and attaching digital signatures.

## Public Key Crypto Standards (PKCS)

- **PKCS#5**: A password-based encryption standard used to derive encryption keys from passwords.
- **PKCS#7**: Used to sign and/or encrypt messages under a PKI.
- **PKCS#11**: Defines a generic API for accessing cryptographic tokens, such as hardware security modules (HSM).
- **PKCS#12**: A file format used for storing private keys and public key certificates, typically protected by a password-based symmetric key.

## Certificate Revocation

- **CRL (Certificate Revocation List)**: A list of certificates that have been revoked by the issuing CA.
- **OCSP (Online Certificate Status Protocol)**: A protocol used to check the status of a digital certificate in real-time.

## TLS Handshake (Full Steps)

1. **Client Hello**: Client sends a request to the server with supported cipher suites and session details.
2. **Server Hello**: Server responds with its chosen cipher suite, certificate, and a public key.
3. **Key Exchange**: Client and server exchange keying material, including pre-master secret (using RSA or Diffie-Hellman).
4. **Authentication and Pre-Master Secret**: Server authenticates with its certificate, and both parties generate the session key.
5. **Session Key Creation**: Both parties create a symmetric session key.
6. **Finished Messages**: Both client and server send encrypted "Finished" messages to confirm the handshake.

## Java Key Stores (JKS) and Trust Store

- **JKS (Java Key Store)**: A repository of cryptographic keys and certificates used in Java applications.
- **Trust Store**: A keystore that stores trusted certificates (typically from CAs) used for verifying the authenticity of incoming certificates.

## TLS Attacks

- **Heartbleed**: A vulnerability in the OpenSSL implementation of TLS that allows attackers to read sensitive memory.
- **POODLE**: An attack that exploits the use of SSLv3 and allows an attacker to decrypt the traffic.

## Cipher Suites

A cipher suite is a collection of cryptographic algorithms used in TLS/SSL protocols for securing communication, including the key exchange algorithm, authentication algorithm, encryption algorithm, and integrity algorithm.

## Perfect Forward Secrecy (PFS)

Perfect Forward Secrecy ensures that session keys are not compromised even if the server's private key is exposed later. Each session generates its own unique key pair.

## HSM Concepts (Hardware Security Module)

- **Dual Control and Split Knowledge**: Requires at least two individuals to manage and operate the HSM for additional security.
- **Backup and Recovery**: Ensures that HSM data and keys can be securely backed up and restored if necessary.
- **HSM Troubleshooting**: Involves identifying and solving issues related to HSM devices, using protocols such as SNMP for monitoring.

## Key Rotation

Key rotation involves periodically changing encryption keys to minimize the impact of a key being compromised. It ensures the continued security of data.

## VPN Security - PPTP

PPTP (Point-to-Point Tunneling Protocol) is an outdated and insecure VPN protocol due to weak encryption and susceptibility to attacks.

## DLP (Data Loss Prevention)

DLP refers to strategies and technologies used to prevent unauthorized access, use, or transmission of sensitive data.
