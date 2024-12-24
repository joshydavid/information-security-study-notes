# Information Security Interview Preparation (Web Application Security - OWASP Top 10)

## Injection Attacks

**SQL injection, Command injection**

```
username = "admin"
password = "' OR 1=1 --"
SELECT * FROM users WHERE username = 'admin' AND password = '' OR 1=1 --'
print("Login successful")
```

Question: “What’s the vulnerability here, and how would you fix it?”
Answer: Command injection; sanitize user_input and use parameterised queries

## Broken Authentication

```

stored_password = "plaintextpassword"
if input_password == stored_password:
print("Login successful")
```

Question: “What are the issues in this login system, and how can it be improved?”
Answer: Store hashed passwords (e.g., bcrypt), implement secure session management (e.g., using tokens).

## Cross-Site Scripting (XSS)

```
const userInput = "<script>alert('XSS')</script>";
document.getElementById("output").innerHTML = userInput;
```

Question: “Why is this vulnerable, and how would you mitigate it?”
Answer: Escape user input before rendering it, use Content Security Policy (CSP).

## Sensitive Data Exposure

`credit_card = "1234-5678-9012-3456"`

Question: “How would you securely handle sensitive data like this?”
Answer: Encrypt the data using AES or RSA, and never store it in plaintext.

## Security Misconfigurations

`app.run(debug=True)`

Question: “What’s the risk of this, and how would you mitigate it?”
Answer: Debug mode reveals sensitive information (stack traces). Disable it in production.

## Broken Access Control

```

@app.route('/admin')
def admin_dashboard():
return "Admin Dashboard"
```

Question: “How would you ensure only authorized users can access this endpoint?”
Answer: Use role-based access control and authentication middleware.

## Cross-Site Request Forgery (CSRF)

```

<form action="/update_profile" method="POST">
    <input type="hidden" name="name" value="hacked">
    <input type="submit">
</form>
```

Question: “How can this attack be mitigated?”
Answer: Use CSRF tokens to verify requests.

## Using Components with Known Vulnerabilities

`from flask import Flask  # Outdated version vulnerable to XXE`

Question: “How do you ensure libraries are secure?”
Answer: Regularly update dependencies and use tools like Dependabot or Snyk.

## Logging and Monitoring

```
if login_failed:
    pass  # No logging
```

Question: “What’s missing here, and why is it important?”
Answer: Log failed logins with enough detail (without sensitive data) for incident detection.

## Buffer Overflows

```
char buffer[10];
strcpy(buffer, "This is a very long string");
```

Question: “What’s the vulnerability here?”
Answer: Buffer overflow. Use functions like strncpy with proper bounds.

## Outdated Cryptography Practices

`hashlib.md5(password.encode()).hexdigest()`

Question: “What’s wrong with this approach?”
Answer: MD5 is insecure. Use modern algorithms like bcrypt, scrypt, or Argon2.
