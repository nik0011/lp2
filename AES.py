from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return ciphertext, cipher.nonce, tag

def aes_decrypt(ciphertext, nonce, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_data.decode('utf-8')

def main():
    # Generate a random 256-bit key using PBKDF2
    password = input("Enter password: ").encode('utf-8')
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32)

    # Message to be encrypted
    message = input("Enter message to encrypt: ")

    # Encrypt the message
    ciphertext, nonce, tag = aes_encrypt(message, key)
    print("Ciphertext:", ciphertext.hex())
    print("Nonce:", nonce.hex())
    print("Tag:", tag.hex())

    # Decrypt the ciphertext
    decrypted_message = aes_decrypt(ciphertext, nonce, tag, key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()