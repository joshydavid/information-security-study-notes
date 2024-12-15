# Information Security Interview Preparation (Cryptography Fundamentals)

## What's the difference between symmetric and asymmetric encryption?

- Symmetric Encryption uses the same key for both encryption and decryption, requires a secure channel to exchange keys.
  - example algorithm AES
  - Pros: Fast and efficient for large data.
  - Cons: Key distribution can be challenging.
- Asymmetric encryption uses a pair of keys, public and private key.
  - Public key is used for encryption and a private key is used for decryption.
  - Some examples include RSA where RSA's security is determined on the product of 2 large prime numbers (p and q) to form the modulus n.
  - It's commonly agreed that if n is large enough, security will not be compromised. However, quantum computing has the power to crack this.
  - Pros: No need for secure key exchange.
  - Cons: Slower than symmetric encryption.

## Why is using SSL/TLS important?

- SSL/TLS ensures secure communication over a network by:
  - Encrypting data in transit: Protects sensitive data (e.g., login credentials) from eavesdropping.
  - Ensuring data integrity: Prevents tampering during transmission.
  - Providing authentication: Uses digital certificates to verify the server’s identity.
  - Prevents man-in-the-middle (MITM) attacks and maintains trust in online communications.

## SSL/TLS Handshake Process

- ClientHello: Client sends SSL/TLS version, cipher and client random.
- ServerHello: Server responds with the chosen cipher, server random and sends its public key to the client.
- KeyExchange:
  - RSA: Client generates a pre-master secret, encrypts it with the server's public key and sends it to the server.
- Session Key Generation:
  - Both the client and server generate the symmetric session keys using the pre-master secret and random values
- Both client and server exchanged finish messages to verify the handshake and start secure communication.
- Data is transmitted securely using symmetric encryption.

## Explain the concept of hashing and how it is different from encryption and encoding

- Hashing is a one-way operation that takes an input and converts it into a fixed-size string of characters, which is typically a hash value known as digest. This is irreversible since it's one way.
- Encryption is a two-way operation, the data is scrambled and transformed into unreadable format but it can later be decrypted and reverted to the original form using the correct key.
- Encoding is the process to transform the data in such a format that can be used by different systems. No keys require to decode, its more for data usability instead of confidentality.

## What are the common hashing algorithms and how do they work?

- Common hashing algorithms include MD5, SHA-1, and SHA-256.
- Hashing creates a fixed-size output (hash) from input data of any size. It is used for data integrity checks and password storage.

## Explain the concept of least privilege and why it’s important in information security

The principle of least privilege means granting users and systems only the minimum level of access needed for them to complete their tasks, this minimises the risk of accidental or malicious damage to sensitive information

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
