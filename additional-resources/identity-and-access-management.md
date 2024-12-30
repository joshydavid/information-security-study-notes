# Identity and Access Management

## Authentication, Authorization, and Identification

1. **Identification**:

   - The process of verifying who the user is, typically by presenting a username, ID, or another identifier.

2. **Authentication**:

   - The process of verifying the identity of a user, typically by validating something the user knows (password), has (OTP, smart card), or is (biometrics).

3. **Authorization**:
   - Determines what an authenticated user is allowed to do (access specific resources, perform certain actions). Authorization occurs after successful authentication.

## Kerberos, SAML, SSO

1. **Kerberos**:

   - A network authentication protocol that uses symmetric key cryptography to authenticate users and services in a secure way. It uses a centralized Key Distribution Center (KDC) to issue tickets for user authentication and service access.

2. **SAML (Security Assertion Markup Language)**:

   - An XML-based framework for exchanging authentication and authorization data between parties, especially between an identity provider (IdP) and a service provider (SP). It is often used for Single Sign-On (SSO) solutions in enterprise environments.

3. **SSO (Single Sign-On)**:
   - A method of authentication that allows users to access multiple applications with a single login session. After logging in once, the user can seamlessly access other authorized applications without re-entering credentials.

## OAUTH

- **OAuth** (Open Authorization) is an authorization framework that allows third-party applications to access a user's resources without sharing their credentials. It uses tokens to grant access to protected resources. OAuth is commonly used in scenarios where an application needs to access data on behalf of the user, such as granting access to a Google account for a third-party app.

## Identity Provider (IdP) Vs Service Provider (SP)

1. **Identity Provider (IdP)**:

   - An entity responsible for authenticating and managing user identities. It verifies the user's credentials and issues authentication tokens or assertions to allow access to services. Examples: Okta, OneLogin, PingIdentity.

2. **Service Provider (SP)**:
   - The entity that provides the services or resources the user wants to access. It trusts the IdP to authenticate the user and grants access based on the authentication assertion.

## Access Control Models

1. **DAC (Discretionary Access Control)**:

   - An access control model where the owner of a resource (such as a file or database) determines who can access it and what actions they can perform. It is based on user discretion and usually relies on Access Control Lists (ACLs).

2. **MAC (Mandatory Access Control)**:

   - A more restrictive model where access to resources is determined by the system based on labels and policies rather than user discretion. It enforces policies such as security clearances (e.g., top secret, secret) and typically uses labels for classification.

3. **RBAC (Role-Based Access Control)**:

   - A model where access rights are assigned based on the user's role within an organization. Each role is associated with a set of permissions, and users inherit the permissions of the roles they are assigned. This simplifies access management for large organizations.

4. **Rule-Based Access Control**:
   - A model where access decisions are based on predefined rules, which are usually set by the administrator. For example, access can be granted based on time of day, the network location of the request, or other contextual information.
