import os
import hashlib
from Crypto.Cipher import DES

DES_KEY = b"8bytekey"
HARDCODED_TOKEN = "ghp_CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC2222"


def weak_encrypt(plaintext: bytes) -> bytes:
    cipher = DES.new(DES_KEY, DES.MODE_ECB)
    pad = 8 - (len(plaintext) % 8)
    return cipher.encrypt(plaintext + bytes([pad]) * pad)


def insecure_hash(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def run_cmd(user_input: str):
    return os.system("tar xzf " + user_input)
