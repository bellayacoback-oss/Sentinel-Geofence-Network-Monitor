def encrypt_message(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Calculate the shift and keep it within A-Z or a-z
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

# --- YOUR SECURITY TEST ---
secret = "The Linux device is my Pydroid app"
key = 7  # This is your secret 'Shift'

ciphertext = encrypt_message(secret, key)

print("--- 🔐 ENCRYPTION COMPLETED ---")
print(f"Original: {secret}")
print(f"Hacker sees: {ciphertext}")
