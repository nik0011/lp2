def encrypt(message, key):
    
    encrypted_text = [''] * key

    for col in range(key):
        pointer = col
        while pointer < len(message):
            encrypted_text[col] += message[pointer]
            pointer += key

    return ''.join(encrypted_text)

def decrypt(ciphertext, key):
    
    num_cols = len(ciphertext) // key

    num_rows = key

    num_extra_chars = len(ciphertext) % key

    decrypted_text = [''] * num_cols

    col = 0
    row = 0
    for symbol in ciphertext:
        
        decrypted_text[col] += symbol

        
        col += 1
        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_extra_chars):
            col = 0
            row += 1

    return ''.join(decrypted_text)

message = "Namaste world "
key = 2

encrypted_message = encrypt(message, key)
print("Encrypted:", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)
