import os

# Audit for specific rogue packages you identified
rogue_apps = [
    "com.samsung.android.cameralyzer", 
    "com.samsung.android.devicekeystring",
    "com.sec.android.app.facatfunction",
    "com.samsung.android.imslogger"
]

def audit_permissions():
    print("--- Sentinel System Audit: Camera Permissions ---")
    for app in rogue_apps:
        # We query the Package Manager (pm) via the shell
        result = os.popen(f"pm list permissions -d -g android.permission.CAMERA").read()
        if app in result:
            print(f"[!] WARNING: {app} has persistent Camera access.")
        else:
            print(f"[✓] {app}: No direct camera link found in this layer.")

audit_permissions()
