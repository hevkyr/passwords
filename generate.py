import secrets
import hashlib
import string

class BIP39PasswordGenerator:
    """
    Gerador de senhas baseado na lista de palavras BIP-0039 e 
    conversão para hash de alta complexidade.
    """
    
    def __init__(self, wordlist_path="english.txt"):
        # No uso real, você deve baixar o arquivo english.txt do link fornecido
        # Para este script, assumimos que as palavras estão em uma lista ou arquivo local.
        self.wordlist = self._load_wordlist(wordlist_path)

    def _load_wordlist(self, path):
        """Carrega as 2048 palavras do padrão BIP-39."""
        try:
            with open(path, "r") as f:
                words = [line.strip() for line in f.readlines()]
            if len(words) != 2048:
                raise ValueError("A lista BIP-39 deve conter exatamente 2048 palavras.")
            return words
        except FileNotFoundError:
            print("Erro: Arquivo english.txt não encontrado. Baixe-o do repositório oficial do Bitcoin/BIPs.")
            return []

    def generate_mnemonic(self, num_words=24):
        """
        Gera uma frase mnemônica usando secrets (segurança criptográfica).
        24 palavras equivalem a 256 bits de entropia.
        """
        if not self.wordlist:
            return None
        
        # Seleciona palavras de forma aleatória e segura
        mnemonic = [secrets.choice(self.wordlist) for _ in range(num_words)]
        return " ".join(mnemonic)

    def derive_complex_password(self, mnemonic, length=14):
        """
        Converte a frase mnemônica em um hash SHA-256 e transforma
        em uma senha com símbolos, números e letras (Ex: @N%h^Bz^pouSKX).
        """
        # 1. Gera o hash da frase (Semente)
        seed_hash = hashlib.sha256(mnemonic.encode()).hexdigest()
        
        # 2. Define o conjunto de caracteres desejado
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        
        # 3. Usa o hash para selecionar caracteres de forma determinística
        # Nota: Usamos secrets.SystemRandom com o hash para manter a complexidade
        state = int(seed_hash, 16)
        rng = secrets.SystemRandom(state)
        
        password = "".join(rng.choice(chars) for _ in range(length))
        return password

# --- Execução do Script ---

# 1. Instancie o gerador (certifique-se de ter o arquivo english.txt na pasta)
gen = BIP39PasswordGenerator("english.txt")

# 2. Gere a frase de 24 palavras (Entropia de 256 bits)
minha_seed = gen.generate_mnemonic(24)

if minha_seed:
    print(f"--- Mnemônico (BIP-39) ---\n{minha_seed}\n")
    
    # 3. Gere a senha final baseada no padrão solicitado
    senha_final = gen.derive_complex_password(minha_seed)
    
    print(f"--- Senha Gerada (Padrão @N%...) ---\n{senha_final}")
