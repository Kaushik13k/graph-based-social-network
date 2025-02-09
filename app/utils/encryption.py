import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from exceptions.exceptions import MessageEncryptionError

SECRET_KEY = os.getenv("AES_SECRET_KEY", None)


class AESEncryption:

    @staticmethod
    def get_key():
        return hashlib.sha256(SECRET_KEY.encode()).digest()

    @staticmethod
    def encrypt(plain_text: str) -> str:
        try:
            key = AESEncryption.get_key()
            cipher = AES.new(key, AES.MODE_CBC)
            cipher_text = cipher.encrypt(
                pad(plain_text.encode(), AES.block_size))
            return base64.b64encode(cipher.iv + cipher_text).decode()
        except Exception:
            raise MessageEncryptionError("encrypting")

    @staticmethod
    def decrypt(encrypted_text: str) -> str:
        try:
            key = AESEncryption.get_key()
            encrypted_data = base64.b64decode(encrypted_text)
            iv = encrypted_data[:AES.block_size]
            cipher_text = encrypted_data[AES.block_size:]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            return unpad(cipher.decrypt(cipher_text), AES.block_size).decode()
        except Exception:
            raise MessageEncryptionError("decrypting")
