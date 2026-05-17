import os

print("--- 📡 SCANNING LOCAL AIRWAVES ---")

# We use the 'Arp' command to see who is talking to the router
try:
    # 'arp -a' shows the IP and MAC addresses of all neighbors
    neighbors = os.popen('arp -a').read()
    if not neighbors:
        print("[!] No neighbors detected. Are you on Mobile Data?")
    else:
        print(neighbors)
except Exception as e:
    print(f"❌ SCAN FAILED: {e}")

print("--- 🏁 SCAN COMPLETE ---")
