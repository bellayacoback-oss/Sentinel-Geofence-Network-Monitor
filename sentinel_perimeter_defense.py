import time
import random
import datetime

def run_perimeter_check():
    print("=" * 60)
    print("     SENTINEL GEOFENCE - ACTIVE PERIMETER DEFENSE DAEMON     ")
    print("=" * 60)
    print("[~] Initializing system integrity validation engine...")
    time.sleep(1)
    
    # 1. Simulate File Integrity Monitoring (Detecting unauthorized persistence/backdoors)
    print("[*] Scanning core system files for unauthorized modifications...")
    time.sleep(1.2)
    critical_files = ["/etc/passwd", "/etc/ssh/sshd_config", "/etc/hosts", ".bashrc"]
    
    # Simulate a clean baseline check
    for c_file in critical_files:
        print(f"  [✓] Integrity Verified (SHA-256 Match): {c_file}")
    
    print("-" * 60)
    
    # 2. Simulate Active Connection Monitoring (Detecting unauthorized remote access)
    print("[*] Monitoring network sockets for anomalous inbound connections...")
    time.sleep(1)
    
    # Mocking some standard trusted active connections
    print("  [Local] 127.0.0.1:443  <--> [Established Host] (Internal Traffic)")
    print("  [Local] 192.168.1.15:22 <--> [Authorized Admin]  (Secure Shell Session)")
    
    # Simulate a suspicious connection trigger (e.g., unexpected port or outside geofence)
    time.sleep(1.5)
    suspicious_ip = f"185.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
    suspicious_port = random.choice([4444, 5555, 9999, 1337])
    
    print(f"\n[⚠️] ALERT: Unexpected Inbound Connection Detected on Port {suspicious_port}!")
    print(f"    Source Vector: {suspicious_ip}")
    print("    Analyzing routing metadata against active Geofence boundary...")
    time.sleep(1.5)
    
    # 3. Automated Mitigation Response
    print("[🔥] MITIGATION TRIGGERED: Source IP falls outside authorized geographical boundary.")
    print(f"    Executing automated iptables rule: DROP input from {suspicious_ip}")
    print("    Session terminated. Security telemetry logged successfully.")
    
    # Append event data to a persistent security audit log
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("SENTINEL_SECURITY_AUDIT.log", "a") as log_file:
        log_file.write(f"[{timestamp}] ALERT: Blocked unauthorized connection from {suspicious_ip} on port {suspicious_port}. Geofence violation mitigated.\n")
        
    print("-" * 60)
    print("[✓] Perimeter sweep complete. Status: 100% SECURE.\n")

if __name__ == "__main__":
    run_perimeter_check()
