# ⚡ passwords

<div align="center">

`BIP39-based high entropy password generator`

### 🛡️ security · 🐍 python · 🤖 automation

| stack | os | focus |
|:---:|:---:|:---:|
| 🐍 Python 3.x | 🐧 Arch · Fedora | 🔐 Cryptography |

</div>

---

## 📖 Sobre o Projeto

Este projeto é um gerador de senhas de alta segurança que utiliza a lista oficial de 2048 palavras do padrão **BIP-39** (usado em carteiras de Bitcoin). O script gera uma frase mnemônica de **24 palavras**, garantindo **256 bits de entropia**, e a converte de forma determinística em uma senha complexa.

### Por que usar BIP-39?
Diferente de geradores comuns, ao guardar sua frase de 24 palavras, você pode regenerar a mesma senha complexa em qualquer dispositivo, eliminando a necessidade de armazenar a senha final em texto claro.

---

## 🚀 Como Usar

### 1. Pré-requisitos
Certifique-se de que o arquivo `english.txt` está no mesmo diretório que o script. Este arquivo contém a wordlist necessária para o funcionamento do algoritmo.

### 2. Instalação
```bash
git clone [https://github.com/hevkyr/passwords.git](https://github.com/hevkyr/passwords.git)
cd passwords


