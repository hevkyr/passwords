import secrets
import hashlib
import string
import random


class BIP39PasswordGenerator:
    def __init__(self, wordlist_path="english.txt"):
        self.wordlist = self._load_wordlist(wordlist_path)

    def _load_wordlist(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                words = [line.strip() for line in f.readlines()]

            if len(words) != 2048:
                raise ValueError("BIP-39 wordlist must contain exactly 2048 words.")

            return words

        except FileNotFoundError:
            print("Error: english.txt not found.")
            return []

    def generate_mnemonic(self, num_words=24):
        if not self.wordlist:
            return None

        mnemonic = [secrets.choice(self.wordlist) for _ in range(num_words)]
        return " ".join(mnemonic)

    def derive_complex_password(self, mnemonic, length=14):
        # deterministic seed
        seed_hash = hashlib.sha256(mnemonic.encode()).digest()

        chars = string.ascii_letters + string.digits + "!@#$%^&*()"

        rng = random.Random(int.from_bytes(seed_hash, "big"))

        password = "".join(rng.choice(chars) for _ in range(length))
        return password


if __name__ == "__main__":
    gen = BIP39PasswordGenerator("english.txt")

    mnemonic = gen.generate_mnemonic(24)

    if mnemonic:
        print(f"--- Mnemonic ---\n{mnemonic}\n")

        password = gen.derive_complex_password(mnemonic)
        print(f"--- Generated Password ---\n{password}")
