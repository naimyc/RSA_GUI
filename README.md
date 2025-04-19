# RSA Cryptosystem in Python

This project is a simple implementation of the RSA algorithm for educational purposes. It includes key generation, encryption/decryption, and digital signatures – all without external libraries.

## 📦 Features
- Generate RSA key pairs
- Encrypt and decrypt messages
- Sign and verify messages
- No third-party libraries required

## 🧠 How RSA works (short version)
1. Generate two large prime numbers
2. Calculate N = p × q and ϕ(N)
3. Choose a public exponent `e`
4. Compute the private key `d` such that `e·d ≡ 1 mod ϕ(N)`

## ▶️ How to Use

```bash
python rsa.py
