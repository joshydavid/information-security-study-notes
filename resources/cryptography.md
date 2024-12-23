# Information Security Interview Preparation (Cryptography Fundamentals)

## Explain the term Cryptography

Cryptography is the practice of using methods to secure sensitive data by transforming readable information, known as plaintext into an unreadable format called ciphertext - through a process called encryption. Only those with the decryption key can convert the ciphertext back into plaintext.

The goal is to protect the confidentiality, integrity and availability of data, ensuring that it remains secure from unauthorized access or tampering whether during storage or transmission.

## Types of Cryptography

**Symmetric Key Cryptography**

- Uses the same key for both encryption and decryption
- E.g AES, DES
- Use case
  - Data-at-rest encryption

**Asymmetric Key Cryptography**

- Uses a pair of keys (public, private)
- E.g RSA
- Use case
  - Secure key exchange
  - Digital signature

**Hybrid Encryption (Envelope Encryption)**

- Combines symmetric and asymmetric cryptography for efficiency and security
- Use case
  - HTTPS (TLS protocol)

**Hashing**

- Converts data into a fixed-size hash known as digest, irreversible, one-way.
- E.g SHA-256
- Use case
  - Password storage
  - Integrity checks

## CIA Triad

The CIA triad is a model in Information Security that emphasizes 3 core principles for protecting data and systems and we need to balance all 3.

**Confidentiality**

- Ensures that sensitive information is accessed only by authorized individuals and not exposed to unauthorized personnel.
- Techniques
  - Encryption
  - Access control
  - Authentication mechanisms

**Integrity**

- Ensures that data remains accurate, consistent and unmodified during storage or transmission by unauthorized personnel.
- Techniques
  - Hashing
  - Digital Signatures
  - Version Control

**Availability**

- Ensures that information and systems are accessible to authorized personnel.
- System must resist disruptions such as cyber attacks, natural disasters or hardware failures.
- Techniques
  - DDoS protection
  - Failover systems
  - Backups

Only the key should be kept secret, the algorithm should be publicly known. (Kerckhoff’s Principle 1883)
Defense is hard, as long as we keep the key secret. Good-enough security is good-enough, certain trade-offs are needed.

## Cryptography Algorithms

- AES
  - Symmetric encryption used for secure data storage and transmission
- RSA
  - Asymmetric encryption for secure key exchange
  - Digital signature
- SHA-256
  - Cryptographic hash function used in certificates and digital signatures
- HMAC
  - Combines hashing with a secret key for message integrity and authenticity

## What's the difference between symmetric and asymmetric encryption?

- Symmetric encryption uses the same key for both encryption and decryption. It requires a secure channel to exchange keys.
  - AES algorithm
  - Pros: Fast and efficient for large data.
  - Cons: Key distribution can be challenging, and the need to have a secure channel to do so.
- Asymmetric encryption uses a pair of keys, public and private key.
  - Public key is used for encryption and a private key is used for decryption.
  - RSA algorithm - where RSA's security is determined on the product of 2 large prime numbers (p and q) to form the modulus n.
  - It's commonly agreed that if n is large enough, security will not be compromised. However, quantum computing has the power to crack this.
  - Pros: No need for secure key exchange.
  - Cons: Slower than symmetric encryption.

Best of both world - envelope encryption.

## Cryptography Concepts Comparison

| RSA Signature                                            | HMAC                                                                |
| -------------------------------------------------------- | ------------------------------------------------------------------- |
| Data Integrity (Asymmetric)                              | Data Integrity (Symmetric)                                          |
| Sender cannot deny, non-repudiation                      | Sender can deny since both share the same key                       |
| Everyone can verify (public key)                         | Only sender and receiver can verify because they share the same key |
| Slow due to big number of computation as it’s asymmetric | Fast cause symmetric                                                |

<br>

|                        | RSA Signature                                                       | RSA Encryption                                                     |
| ---------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Sender (Private key)   | Yes, sender needs private to sign the message                       | No, sender just needs receiver’s public key to encrypt the message |
| Receiver (Private key) | No, receiver just needs sender’s public key to verify the signature | Yes, receiver requires its private key to decrypt                  |
| Limitation             | None, can sign on any size (signs on the digest, the hash)          | Only encrypt data smaller than modulus n                           |

## Why is using SSL/TLS important?

- SSL/TLS ensures secure communication over a network by:
  - Encrypting data in transit: Protects sensitive data (e.g., login credentials) from eavesdropping.
  - Ensuring data integrity: Prevents tampering during transmission.
  - Providing authentication: Uses digital certificates to verify the server’s identity.
  - Prevents man-in-the-middle (MITM) attacks and maintains trust in online communications.

## SSL/TLS Handshake Process

RSA key exchange process

- Client Hello: Client sends a message to the server containing
  - SSL/TLS version it supports
  - list of cipher suites
  - a random value called client random
- Server Hello: The Server responds with
  - the chosen cipher
  - a random value called server random server random
  - its public key (from its certificate) which includes the server's identity
- Key Exchange:
  - The client
  - generates a pre-master secret
  - encrypts it with the server's public key and
  - sends it to the server.
- Session Key Generation:
  - Server: Decrypt the pre-master secret using its private key, combine it with client random and server random to derive the symmetric key
  - Client: Combine the pre-master secret with client random and server random to derive the symmetric key
- Handshake Completion:
  - Both the client and server sends a finished message, which includes an encrypted hash of all previous handshake messages.
- Secure Communication:
  - Data is transmitted securely using symmetric encryption.

## Explain the concept of hashing and how it is different from encryption and encoding

- Hashing is a one-way operation that takes an input and converts it into a fixed-size string of characters, which is typically a hash value known as digest. This is irreversible since it's one way.
- Encryption is a two-way operation, the data is scrambled and transformed into unreadable format but it can later be decrypted and reverted to the original form using the correct key.
- Encoding is the process to transform the data in such a format that can be used by different systems. No keys require to decode, its more for data usability instead of confidential.

## Explain the concept of least privilege and why it’s important in information security

The principle of least privilege means granting users and systems only the minimum level of access needed for them to complete their tasks, this minimizes the risk of accidental or malicious damage to sensitive information

## What is multi-factor authentication (MFA) and why is it important?

MFA requires multiple forms of authentication, such as:

- Something you know: Password or PIN.
- Something you have: Security token or smartphone.
- Something you are: Biometric data like fingerprints or facial recognition.

## What is authentication?

- **Definition:** Authentication is the process of verifying the identity of a user, system, or entity. It ensures that the person or system claiming to be something is actually who or what they say they are.

- **How It Works:**

  - When a user attempts to access a system, the system will ask for credentials (e.g., username/password, security token, or biometric data).
  - These credentials are then compared to those stored in a database to confirm identity.

- **Examples of Authentication:**
  - **Password-based:** Traditional method where a password (often with a username) is used to gain access.
  - **Biometric:** Using physical characteristics like fingerprints, face recognition, or iris scans.
  - **Token-based:** Using hardware or software tokens, often used in MFA (multi-factor authentication).
  - **Certificate-based:** Using digital certificates for system authentication, often seen in SSL/TLS.

## What is authorization?

- **Definition:** Authorization is the process that determines what an authenticated user can and cannot do within a system. It occurs after authentication and ensures that users can only access resources they are permitted to use.

- **How It Works:**
  - Once the user is authenticated, their permissions (access rights) are checked against the system's policy to determine what actions they can perform.
  - Common methods include role-based access control (RBAC), attribute-based access control (ABAC), or access control lists (ACLs).

## What is the difference between authentication and authorization?

- **Authentication:** Verifies identity (e.g., "Who are you?").
- **Authorization:** Grants access to resources based on identity (e.g., "What are you allowed to do?").

## What is multi-factor authentication (MFA)?

- **Definition:** Multi-factor authentication is a security mechanism that requires two or more forms of verification before granting access to a system.

- **Types of Factors in MFA:**

  1. **Something you know:** A password, PIN, or passphrase.
  2. **Something you have:** A smartcard, mobile device, or hardware token.
  3. **Something you are:** Biometric factors such as fingerprints, voice recognition, or face scans.
  4. **Somewhere you are:** Geolocation (often used for geofencing in combination with other factors).
  5. **Something you do:** Behavioral biometrics, such as how you type or use a mouse.

- **Why MFA is important:**

  - It adds layers of security, making it harder for attackers to gain unauthorized access, even if one factor (like a password) is compromised.

- **Common MFA Methods:**
  - **SMS-based:** A one-time passcode (OTP) sent to the user’s mobile device.
  - **App-based:** Using an authenticator app (e.g., Google Authenticator, Authy) to generate one-time codes.
  - **Hardware token:** A physical device that generates OTPs or uses a protocol like U2F (Universal 2nd Factor).
  - **Push notifications:** A push notification to a mobile device where the user approves or denies the login attempt.

## Single Sign-On (SSO)

- **Definition:** SSO is an authentication process that allows a user to access multiple applications with a single set of credentials.

- **How It Works:**

  - Once a user logs in to one application, they can automatically access other connected applications without needing to log in again. SSO uses a central authentication server that manages the user's identity and credentials.

- **Examples of SSO protocols:**

  - **SAML (Security Assertion Markup Language):** A widely used XML-based protocol for exchanging authentication and authorization data between systems.
  - **OAuth and OpenID Connect:** OAuth is an authorization framework, and OpenID Connect is an identity layer on top of OAuth.

- **Benefits of SSO:**
  - Reduces password fatigue for users.
  - Centralized authentication and easier management of user accounts.
  - Improved security (fewer passwords to manage and remember).

## OAuth and OpenID Connect (OIDC)

- **OAuth (Authorization Protocol):**

  - OAuth is a protocol for authorizing third-party applications to access user data without sharing credentials.
  - It uses access tokens for authorization and scopes to limit the level of access granted.

  **How OAuth works:**

  - A user logs into a service (e.g., Google or Facebook).
  - The third-party app requests permission to access some of the user’s data (e.g., profile info, email).
  - The user grants or denies permission, and if granted, an access token is issued to the app.

- **OpenID Connect (OIDC) (Authentication Protocol):**
  - OpenID Connect is built on top of OAuth and adds an authentication layer, allowing the application to verify the user’s identity.
  - It includes an ID token (JWT - JSON Web Token) that contains user information.

## Role-Based Access Control (RBAC)

- **Definition:** RBAC is an access control model that assigns users to roles, and each role has permissions associated with it. The users inherit permissions based on their role.

- **How It Works:**

  - Users are assigned roles (e.g., Admin, User, Guest).
  - Each role is granted a set of permissions (e.g., read, write, execute).
  - Access to resources is determined by the user's role rather than their individual identity.

- **Benefits:**
  - Simplifies user management.
  - Enhances security by enforcing least privilege.
  - Easier to audit and enforce policies.

## Identity and Access Management (IAM)

- **Definition:** IAM refers to the framework of policies, technologies, and systems that manage and monitor digital identities and their access to various resources in an organization.

- **Key Components of IAM:**

  1. **Identity Management:** Creating, managing, and maintaining user identities.
  2. **Authentication:** Verifying the identity of users.
  3. **Authorization:** Managing the permissions and access rights granted to users.
  4. **User Provisioning/De-provisioning:** Automatically creating and deleting accounts based on user lifecycle events (e.g., hiring, firing, role change).

- **Examples of IAM solutions:**
  - Active Directory (AD)
  - Okta
  - Azure Active Directory (Azure AD)

## Federated Identity Management

- **Definition:** Federated identity management (FIM) allows users to access multiple systems across different domains with a single set of credentials.

- **How It Works:**

  - A trusted identity provider (e.g., Google, Microsoft) authenticates the user, and the relying party (service provider) accepts the identity assertion.

- **Protocols for FIM:**
  - **SAML**: As mentioned earlier, SAML is often used for web-based single sign-on across different security domains.
  - **OAuth/OpenID Connect**: Common for API and mobile application authentication.

## Password Policies and Security

- **Password Strength:** Enforcing strong password policies, such as:

  - Minimum length (e.g., 8-12 characters).
  - Requirement for complexity (uppercase, lowercase, numbers, special characters).

- **Password Hashing:** Storing passwords securely by hashing them with algorithms like bcrypt, PBKDF2, or Argon2. This ensures that passwords are not stored in plaintext.

- **Password Storage Best Practices:**
  - Use salt to make hashed passwords unique.
  - Do not store or transmit passwords in plaintext.
  - Use multi-factor authentication as an additional layer of protection.

## Public Key Infrastructure (PKI)

- Framework for managing digital keys and certificate used for securing communications.
- Asymmetric cryptography, consists of a public and private key

### Public Key

- Shared openly and can be used by anyone
  - to encrypt messages
  - to verify digital signatures created by the corresponding private key
- Can be distributed widely without compromising security, it's public

### Private Key

- Kept secret and is used
  - to decrypt message encrypted with the corresponding public key
  - to create digital signature, proving authenticity and integrity => non-repudiation as well
- Must be safeguarded because anyone with the private key can used it to read encrypted message or sign malicious data

In PKI, digital certs issued by CA contain the public key and information about the owner. Anyone who wants to send an encrypted message to this owner can use the owner's public key and only he can decrypt using his private key.

## Scenario 1 - Symmetric Encryption in Secure File Storage

**A company stores sensitive files on a server. How would you recommend securing these files using symmetric encryption? What challenges might arise?**

- Use AES encryption to encrypt the files with a strong symmetric key.
- Store the key in a secure hardware module such as HSM
- Challenges
  - Key management, ensuring secure distribution and rotation of encrypted keys
  - Access control, limiting who has and can access they keys and encrypted files.

## Scenario 2 - Secure Communication via TLS

**During a TLS handshake, an attacker performs a man-in-the-middle (MITM) attack by presenting a fake certificate. How can the client detect this?**

- The client can detect a fake certificate by validating it against trusted Certificate Authorities (CAs) in the certificate store.
- TLS uses the chain of trust to ensure that the server's certificate is signed by a CA that the client trusts.

## Scenario 3 - Password Hashing Vulnerability

**A developer stores user passwords in a database using MD5. Why is this insecure, and what would you recommend instead?**

- MD5 is insecure due to its vulnerability to collision attacks and fast computation, making it susceptible to brute force.
- Use secure hashing algorithms such as bcrypt, Argon2 with a unique salt for each password such that even if 2 passwords are the same, the hashed password also known as digest will be different.

## Scenario 4 - Secure API Authorization

**How would you implement secure authorization for a REST API handling sensitive user data?**

- Use OAuth2.0 for secure access delegation (Sign in with Apple)
- Issue access tokens with scopes to limit access.
- Use HTTPS to encrypt API communication from client to server.
- Rotate and expire tokens regularly to mitigate issues.

## Scenario 5 - Incident with Compromised Certificate

**A website’s TLS certificate is compromised. What steps should be taken to secure the communication?**

- Revoke the compromised certificate using the CA's certificate revocation mechanism.
- Issue a new certificate.
- Investigate the root cause of the compromise.

## Scenario 6 - Hybrid Encryption System Design

**Design a secure file transfer system using both symmetric and asymmetric encryption.**

- Generate a random symmetric key for file encryption using AES
- Encrypt the symmetric key with the recipient's public key using RSA
- Transmit the encrypted file and the encrypted key
- The recipient uses their private key to decrypt the symmetric key, and then use the symmetric key to decrypt the encrypted file.
