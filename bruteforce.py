# --- OFFICIAL BRUTE FORCE MODULE ---
ciphertext = "Ymj Qnszc ijanhj bfx ozxy rd Udiwtni fuu"

print("📡 ATTACK STARTING...\n")

for key in range(1, 26):
    attempt = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Reverse the shift
            attempt += chr(start + (ord(char) - start - key) % 26)
        else:
            attempt += char
    
    # Check for keywords to identify the win
    if "Linux" in attempt:
        print(f"🔓 KEY {key:02}: {attempt} <-- SUCCESS!")
    else:
        print(f"❌ KEY {key:02}: {attempt}")

print("\n--- 🏁 ATTACK COMPLETE ---")
