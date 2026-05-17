import subprocess

# The target packages we identified in the previous audit
targets = [
    "com.samsung.android.imslogger",
    "com.samsung.android.cameralyzer",
    "com.sec.android.app.facatfunction"
]

print("--- SENTINEL SUITE: DYNAMIC TRAFFIC AUDIT ---")

def get_uid(package):
    """Retrieves the Unique ID for a package."""
    cmd = f"rish -c 'dumpsys package {package} | grep userId'"
    res = subprocess.check_output(cmd, shell=True).decode()
    return res.split('=')[1].split()[0]

for pkg in targets:
    try:
        uid = get_uid(pkg)
        # Pulling network stats for this specific UID
        stat_cmd = f"rish -c 'dumpsys netstats detail | grep \"uid={uid}\"'"
        stats = subprocess.check_output(stat_cmd, shell=True).decode()
        
        if stats:
            print(f"[!] Traffic Detected for {pkg} (UID: {uid})")
            print(f"    Raw Stats: {stats.strip()[:100]}...") 
        else:
            print(f"[✓] {pkg}: No network activity recorded.")
    except Exception:
        print(f"[?] {pkg}: Could not retrieve network stats.")

print("--- AUDIT COMPLETE ---")
