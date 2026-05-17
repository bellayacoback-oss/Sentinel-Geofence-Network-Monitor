import os
import datetime

# 1. Configuration: What are we looking for?
SENSITIVE_KEYWORDS = ['password', 'secret', 'key', 'token', 'config', '.log']
TARGET_DIR = '/sdcard/Documents' # Change to the directory you want to audit

def audit_files():
    print(f"--- System Sentinel Audit Started: {datetime.datetime.now()} ---")
    print(f"Scanning Directory: {TARGET_DIR}\n")
    
    suspicious_finds = []

    try:
        for root, dirs, files in os.walk(TARGET_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                
                # Check 1: Sensitive file extensions or names
                if any(key in file.lower() for key in SENSITIVE_KEYWORDS):
                    suspicious_finds.append(f"[!] SENSITIVE NAME: {file_path}")

                # Check 2: Hidden files (starting with a dot)
                if file.startswith('.'):
                    suspicious_finds.append(f"[!] HIDDEN FILE: {file_path}")

        # Summary of results
        if suspicious_finds:
            for item in suspicious_finds:
                print(item)
        else:
            print("No immediate file-level threats detected in target directory.")

    except PermissionError:
        print("Error: Permission denied. Please ensure Pydroid has Storage access.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    audit_files()
