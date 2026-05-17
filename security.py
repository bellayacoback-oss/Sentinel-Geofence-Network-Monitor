import os

# ==============================
# 🕵️ COMPROMISE DETECTOR v5.1
# ==============================

def scan_for_leaks():
    print("--- 🔍 SCANNING FOR OUTLOOK SYNC ---")
    
    # Targeting the OneDrive path we found in your environment variables
    #
    target_account = "Bellatosoro@outlook.com"
    potential_paths = [
        "/sdcard/Android/data/com.microsoft.skydrive",
        "/sdcard/Download/Outlook_Data"
    ]
    
    for path in potential_paths:
        if os.path.exists(path):
            print(f"🚩 ALERT: Local data found for {target_account} at {path}")
            print("Action: Delete folder after backup.")
        else:
            print(f"✅ CLEAN: {path} not detected locally.")

    print("\n--- 🛡️ SYSADMIN ACTION ---")
    print("Change your Google Recovery Email")
    print("to a NEW address if Outlook was used for recovery.")

if __name__ == "__main__":
    scan_for_leaks()
