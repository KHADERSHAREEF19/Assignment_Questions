# Assignment 2: RSA Cryptographic Key Generation

This assignment focuses on the practical generation of asymmetric keys using the OpenSSL command-line tool. This is a foundational skill in cybersecurity for securing data transmission and identity verification.

## 🛠️ Tasks Completed

### 1. Generate RSA Private Key
Generated a 2048-bit RSA private key.
- **Command:** `openssl genrsa -out privatekey.pem 2048`

### 2. Export Public Key
Derived the corresponding public key from the private key.
- **Command:** `openssl rsa -in privatekey.pem -pubout -out publickey.pem`

### 3. Key Format Verification
Verified that both keys were exported in the **PEM (Privacy Enhanced Mail)** format
- **Private Key Header:** `-----BEGIN RSA PRIVATE KEY-----`
- **Public Key Header:** `-----BEGIN PUBLIC KEY-----`



## 🔍 Understanding the Process
In this asymmetric setup, the **Public Key** can be given to anyone to encrypt data, but only the holder of the **Private Key** can decrypt that data. This ensures the "Confidentiality" pillar of the CIA triad (Confidentiality, Integrity, and Availability).
