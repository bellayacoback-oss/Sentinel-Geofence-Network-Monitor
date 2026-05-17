import time

# Dictionary of high-risk permissions and their "Threat Weight"
THREAT_DATABASE = {
    "android.permission.READ_SMS": 40,
    "android.permission.RECEIVE_SMS": 50,
    "android.permission.RECORD_AUDIO": 30,
    "android.permission.CAMERA": 25,
    "android.permission.ACCESS_FINE_LOCATION": 20,
    "android.permission.READ_CONTACTS": 15,
    "android.permission.SYSTEM_ALERT_WINDOW": 60, # Overlay permission (very dangerous)
}

def analyze_app_risk(app_name, permissions):
    print(f"\n🔍 AUDITING: {app_name}")
    print("-" * 30)
    
    total_score = 0
    flagged = []

    for p in permissions:
        if p in THREAT_DATABASE:
            weight = THREAT_DATABASE[p]
            total_score += weight
            flagged.append(f"⚠️ {p} (+{weight})")
        else:
            print(f"✅ Safe Permission: {p}")

    # Display results
    for f in flagged:
        print(f)
        
    print(f"\n📊 FINAL PRIVACY RISK SCORE: {total_score}")
    
    if total_score >= 80:
        print("🚨 STATUS: CRITICAL RISK - Possible Spyware/Keylogger behavior.")
    elif total_score >= 40:
        print("⚠️ STATUS: ELEVATED RISK - App overreaching on privacy.")
    else:
        print("🟢 STATUS: LOW RISK - Typical app behavior.")

# --- SIMULATION SECTION ---
# This simulates what a real scan would find. 
# You can change these lists to match apps you find on your phone!

# Example 1: A suspicious "Flashlight" app
analyze_app_risk("Super Flashlight 2026", [
    "android.permission.CAMERA", 
    "android.permission.READ_SMS", 
    "android.permission.SYSTEM_ALERT_WINDOW"
])

time.sleep(1)

# Example 2: A standard Messaging app
analyze_app_risk("Secure Messages", [
    "android.permission.READ_CONTACTS", 
    "android.permission.READ_SMS",
    "android.permission.RECEIVE_SMS"
])
"android.permission.delete.FLASHLIGHT""