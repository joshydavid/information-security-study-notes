# Web Application Security - OWASP Top 10

## Injection Attacks

### SQL injection, Command injection

```
username = "admin"
password = "' OR 1=1 --"
SELECT * FROM users WHERE username = 'admin' AND password = '' OR 1=1 --'
print("Login successful")
```

### What’s the vulnerability here, and how would you fix it?

- Command injection
- Sanitize user_input
- Use parameterised queries

## Broken Authentication

```
stored_password = "plaintextpassword"
if input_password == stored_password:
print("Login successful")
```

### What are the issues in this login system, and how can it be improved?

Store hashed and salted passwords (e.g., bcrypt)

## Cross-Site Scripting (XSS)

```
const userInput = "<script>alert('XSS')</script>";
document.getElementById("output").innerHTML = userInput;
```

### Why is this vulnerable, and how would you mitigate it?

- Validate all user inputs
- Escape user input before rendering it
- Use Content Security Policy (CSP, choose which domain and resources are allowed to load and execute scripts)
- Use secure and modern JavaScript frameworks
- Use `httpOnly` flag on cookies to prevent JavaScript from accessing the cookies

## Sensitive Data Exposure

`credit_card = "1234-5678-9012-3456"`

### How would you securely handle sensitive data like this?

Encrypt the data using AES or RSA, and never store it in plaintext.

## Security Misconfigurations

`app.run(debug=True)`

### What’s the risk of this, and how would you mitigate it?

Debug mode reveals sensitive information (stack traces). Disable it in production.

## Broken Access Control

```
@app.route('/admin')
def admin_dashboard():
return "Admin Dashboard"
```

## How would you ensure only authorized users can access this endpoint?

Use role-based access control and authentication middleware.

## Cross-Site Request Forgery (CSRF)

```
<form action="/update_profile" method="POST">
    <input type="hidden" name="name" value="hacked">
    <input type="submit">
</form>
```

## How can this attack be mitigated?

- Use CSRF tokens (SHA-256 hash) to verify requests.
- Use secure cookies
  - Set `httpOnly` flag to true so that JavaScript cannot access the cookies.
  - Set secure flag for cookies to ensure they are only transmitted via HTTPS, encrypted connection to prevent man-in-the-middle attacks.

## Using Components with Known Vulnerabilities

`from flask import Flask  # Outdated version vulnerable to XXE`

### How do you ensure libraries are secure?

Regularly update dependencies and use tools like Dependabot or Snyk.

## Logging and Monitoring

```
if login_failed:
    pass  # No logging
```

### What’s missing here, and why is it important?

Log failed logins with enough detail (without sensitive data) for incident detection.

## Buffer Overflows

Buffer overflow occurs when a program writes more data to a buffer (a fixed-size memory region) than it can hold, causing the excess data to overwrite adjacent memory. This vulnerability can be exploited by attackers to alter the program’s behavior, crash it, or even execute malicious code.

Mitigation:
Check the size of the data being written to the buffer, else the attacker can provide input larger than the buffer size, causing an overflow

```
char buffer[10];
strcpy(buffer, "This is a very long string");
```

### What’s the vulnerability here?

Buffer overflow. Use functions like strncpy with proper bounds.

## Outdated Cryptography Practices

`hashlib.md5(password.encode()).hexdigest()`

### What’s wrong with this approach?

- MD5 is insecure due to its vulnerability to collisions.
- Use modern algorithms like bcrypt, scrypt, or Argon2.
