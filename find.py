import os

print("--- 🕵️ BACKGROUND PROCESS AUDIT ---")

# This command lists 'Top' processes currently using CPU/Memory
# On Android, we filter for apps that aren't system-critical
try:
    processes = os.popen('ps -A').read().split('\n')
    print(f"[ OK ] Total Processes Detected: {len(processes)}")
    
    print("\n[!] Top 5 Potential Data Users:")
    # We look for common 'Trackers' or Social apps
    for p in processes:
        if 'google' in p or 'facebook' in p or 'meta' in p:
            print(f"   -> Found: {p.split()[-1]}")
            
except Exception as e:
    print(f"[ FAIL ] Permission Denied: {e}")

print("\n--- 🏁 AUDIT COMPLETE ---")
