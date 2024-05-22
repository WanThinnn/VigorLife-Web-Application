from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

def encrypt_data(key, iv, plaintext):
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(iv, plaintext, None)
    return urlsafe_b64encode(iv + ciphertext)

def decrypt_data(key, ciphertext):
    aesgcm = AESGCM(key)
    ciphertext = urlsafe_b64decode(ciphertext)
    iv = ciphertext[:12]  # Extract the IV
    ciphertext = ciphertext[12:]  # Extract the ciphertext
    plaintext = aesgcm.decrypt(iv, ciphertext, None)
    return plaintext

def get_key():
    key = input("Enter your AES GCM key: ").encode('utf-8')
    return key

def get_iv():
    iv = input("Enter your AES GCM IV (12 bytes): ").encode('utf-8')
    return iv

# key, iv = get_key_iv()
# Dữ liệu cần mã hóa
# plaintext = b'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'

# # Mã hóa dữ liệu
# encrypted_data = encrypt_data(b'thientaiquanphuongthinh204@#$uit', b'uit@vnu#hcm%', plaintext)
# print("Encrypted data:", encrypted_data)

# # Giải mã dữ liệu
# decrypted_data = decrypt_data(b'thientaiquanphuongthinh204@#$uit', encrypted_data)
# print("Decrypted data:", decrypted_data.decode('utf-8'))