# ⚡ passwords

<div align="center">

**Deterministic password generator using BIP-39 wordlists**

🛡️ security • 🐍 python • 🔐 cryptography

</div>

---

## 📖 About

`passwords` is a deterministic password generator that uses the official **BIP-39 English wordlist** as entropy source.

The script:

- Generates a 24-word mnemonic phrase
- Hashes the mnemonic using SHA-256
- Uses the hash as deterministic seed for password generation

This allows you to regenerate the same password anytime using only your mnemonic phrase.

> This project uses the BIP-39 wordlist only.  
> It is **not** a cryptocurrency wallet or seed generator.

---

## ✨ Features

- 24-word mnemonic generation
- Deterministic password derivation
- SHA-256 hashing
- Offline usage
- No external dependencies

---

## 🚀 Installation

```bash
git clone https://github.com/hevkyr/passwords.git
cd passwords
```

---

## ▶ Usage

Place `english.txt` in the same directory and run:

```bash
python3 generate.py
```

---

## 💻 Example Output

```text
--- Mnemonic ---
dizzy liquid parade orbit paper anchor ...

--- Generated Password ---
A9@kT!x3Lm#Q8p
```

---

## 🔬 How it works

1. Randomly select 24 words from BIP-39 wordlist
2. Join into mnemonic string
3. Hash mnemonic with SHA-256
4. Convert hash into deterministic PRNG seed
5. Generate password from letters, numbers, and symbols

---

## ⚠ Security Notes

- Never share your mnemonic
- Store it offline
- Anyone with the mnemonic can regenerate your password

---

## 📜 License

MIT
