# Encryption and Authentication

## What is a three-way handshake?

A three-way handshake is the process used to establish a TCP connection between a client and a server.

**Step 1**
The client sends a `SYNC` packet to the server to initiate the connection.

**Step 2**
The server responds with a `SYNC-ACK` packet, which confirms the client's request indicate readiness to communicate.

**Step 3**
The client sends an `ACK` package to the server, completing the handshake and establishing the connection.

## What is a cookie and how does it work?

A cookie is a small piece of data sent from a server, and stored in the user's browser which is used to remember information about the user.

- Can keep users logged in
- Can remember users' preferences and settings
- Can be used for analytics and tracking user behaviour

The server sends cookies via HTTP headers, and the browser sends cookies back with each subsequent request to the same domain.

## What is a session and how does it work?

A session is a server-side data structure used to store information about a user's interaction with the website/application. Does not need user to be authenticated for session to work.

- User visits a website, the server creates a unique `sessionId` stored in a cookie.
- The `sessionId` is sent with each subsequent request, allowing the server to retrieve the corresponding session data.
- Sessions aer stored server-side, cookies are stored on the client-side.

## Explain how OAuth Works

OAuth is an authorisation protocol that allows third-party applications to accept user data without exposing the user's credentials.

- The user is redirected to an authorization server where they grant access to their data
- The server redirects the user back to the client application with an authorization code.
- The client application exchanges the authorization code for an access token.
- The client uses the access token to make API requests on behalf of the user.

## Explain how JWT Works

- Client logins and authenticated by the server
- Server generates a JWT token and sends it to the client
- Client stores the token (local storage, session storage, cookies). Best stored in HttpOnly cookies to prevent XSS.
- Client includes this token in the Authorization header of each API request. `Authorization: Bearer <token>`
- Server validates the token's signature, checks the expiry and verifies other claims

## What is a public key infrastructure flow?

It is a framework for managing public-key encryption, including key pairs and digital certificates.

- A user or system generates a key pair (public and private keys).
- The public key is registered with a Certificate Authority (CA), which issues a digital certificate.
- The certificate is used for encryption/decryption or digital signing.
- The CA ensures the authenticity of the public key through its certificate.

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

## Can you explain how the SSL/TLS handshake process works?

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

## How does HMAC work?

HMAC (Hash-Based Message Authentication Code) is a mechanism for verifying data integrity and authenticity using a cryptographic hash function combined with a secret key.

- The message is combined with a secret key.
- The result is hashed using a cryptographic hash function (e.g., SHA-256).
- The resulting hash is sent with the message to the recipient.
- The recipient hashes the message with the same key and compares it to the provided hash. If they match, the message is verified.

## Why is HMAC designed in that way?

- Purpose: HMAC is designed to ensure both data integrity (verifying the message has not been tampered with) and authenticity (verifying the sender is legitimate). Does not fulfil confidentiality.

- Security: The combination of a secret key and hash function makes it resistant to attacks such as brute-forcing and collision attacks.

## What’s the difference between Diffie-Hellman and RSA?

**Diffie-Hellman**

- Purpose: Used for key exchange over an insecure channel. It allows two parties to agree on a shared secret key.
- Asymmetric but no encryption/decryption.

**RSA**

- Purpose: Used for both key exchange and encryption/decryption.
- Asymmetric encryption system based on the difficulty of factoring large numbers.

## If you're going to compress and encrypt a file, which one do you do first and why?

- Compress first, then encrypt.
- Reason: Compression reduces the file size by removing redundant data, making the encryption process more efficient. If you encrypt first, the data will be randomized, making it difficult to compress effectively.

## How do I authenticate you and know you sent the message?

- Authentication: Verifying your identity through something you know (password), something you have (token), or something you are (biometrics).
- Message Integrity: Use digital signatures (e.g., RSA or HMAC) to ensure that the message came from you and hasn’t been altered.

## Should you encrypt all data at rest?

Yes. Encrypting data at rest helps protect sensitive information from unauthorized access, especially if physical security of storage devices is compromised (e.g., theft of hard drives).

## What is perfect forward secrecy?

**Definition**
Perfect Forward Secrecy (PFS) ensures that even if a private key is compromised in the future, past communications remain secure.

**How It Works**
PFS uses ephemeral key exchange methods (e.g., Diffie-Hellman) to generate new session keys for each communication, ensuring that past sessions cannot be decrypted if the private key is later exposed.
