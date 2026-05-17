import subprocess

def check_duplicates():
    print("--- 🔍 DUPLICATE PACKAGE AUDIT ---")
    result = subprocess.check_output(['pm', 'list', 'packages']).decode().split('\n')
    
    # Clean the list
    packages = [line.replace('package:', '').strip() for line in result if line]
    
    # Check for suspicious naming patterns (e.g., two apps named 'Camera')
    print("Checking for package name overlaps...")
    # Add any app name you are seeing duplicates of here:
    target_names = ['camera', 'gallery', 'settings', 'phone', 'message']
    
    for target in target_names:
        matches = [p for p in packages if target in p.lower()]
        if len(matches) > 1:
            print(f"\n📍 Found multiple '{target}' related packages:")
            for m in matches:
                print(f"  -> {m}")
        else:
            print(f"✅ {target.capitalize()}: No suspicious duplicates.")

check_duplicates()
