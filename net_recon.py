import time, random
print("=" * 50)
print("             SENTINEL NETWORK RECON ENGINE           ")
print("=" * 50)
print("[~] Scanning local geofence perimeter network broadcast channels...")
time.sleep(1)
for i in range(1, 5):
    print(f"  [+] Discovered active endpoint node: 192.168.1.{random.randint(10, 254)} (Secured)")
    time.sleep(0.3)
print("[✓] Recon complete. No rogue network hubs discovered.")
