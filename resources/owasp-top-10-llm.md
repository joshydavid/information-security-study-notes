# Web Application Security - OWASP Top 10 for Large Language Models (LLMs)

## 1. Prompt Injection

Manipulate LLMs via crafted inputs can lead to unauthorized access, data breaches, and compromised decision-making.
**Prevention**

- Principle of Least Privilege
- Human in the Loop
- Segregate Content Prompt
- Trust Boundaries

## 2. Insecure Output Handling

Neglecting to validate LLM outputs may lead to downstream security exploits, including code execution that compromises systems and exposes data. Instead of `SELECT`, it `DROPS table`

**Prevention**

- Do not assume that LLM is a trusted user
- Validate user input, don't just trust but also verify

## 3. Training Data Poisoning

Tampered training data can impair LLM models leading to responses that may compromise security, accuracy, or ethical behavior.
Otherwise, garbage in, garbage out.

**Prevention**

- Know the sources and ensure that they are not compromised
- Verify info
- Validate results
- Wash, rinse, repeat

## 4. Model Denial of Service

Overloading LLMs with resource-heavy operations can cause service disruptions and increased costs.

**Prevention**

- Rate-limiting
- Input validation and restrict the input length
- Implement circuit breaker

## 5. Supply Chain Vulnerabilities

Depending upon compromised components, services or datasets undermine system integrity, causing data breaches and system failures.

**Prevention**

- Use cryptographic checks (e.g., hashes, digital signatures) to verify the integrity of datasets and model updates.
- Limit access to external resources
- Secure model hosting

## 6. Sensitive Information Disclosure

Failure to protect against disclosure of sensitive information in LLM outputs can result in legal consequences or a loss of competitive advantage.

**Prevention**

- Access control
- Monitor and log outputs

## 7. Insecure Plugin Design

LLM plugins processing untrusted inputs and having insufficient access control risk severe exploits like remote code execution

**Prevention**

- Sandbox plugins
- Access control
- Secure communication

## 8. Excessive Agency

Granting LLMs unchecked autonomy to take action can lead to unintended consequences, jeopardizing reliability, privacy, and trust.

**Prevention**

- Require human approval
- Action whitelisting
- Audit trail

## 9. Overreliance

Failing to critically assess LLM outputs can lead to compromised decision making, security vulnerabilities, and legal liabilities. LLMs are prone to hallucinations.

**Prevention**

- Understand limits
- Train users
- Verify sources

## 10. Model Theft

Unauthorized access to proprietary large language models risks theft, competitive advantage, and dissemination of sensitive information.

**Prevention**

- Encrypt model files at rest and in transit to prevent unauthorized access.
- Access control
- API rate limiting amd monitoring
- Watermarking
- Zero trust principle
- Legal protection
- Regular penetration testing
