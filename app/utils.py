from cryptography.fernet import Fernet

# Generate encryption key (Keep this safe in production)
FERNET_KEY = Fernet.generate_key()
fernet = Fernet(FERNET_KEY)

def encrypt_data(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()
