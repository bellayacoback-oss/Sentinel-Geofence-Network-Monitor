import time
import socket
import json

# 1. Geofencing Coordinates Baseline
SAFE_ZONE_LAT = 49.1913   # Example coordinates
SAFE_ZONE_LON = -122.8490
GEofence_RADIUS = 0.005   # Coordinate tolerance variance

def get_current_location():
    """
    Simulates fetching device hardware location telemetry.
    In a live Termux environment, this calls 'termux-location'.
    """
    # For baseline testing, we return safe coordinates
    return 49.1913, -122.8490 

def check_geofence(lat, lon):
    """Calculates if the device is inside the designated perimeter."""
    lat_delta = abs(lat - SAFE_ZONE_LAT)
    lon_delta = abs(lon - SAFE_ZONE_LON)
    if lat_delta <= GEofence_RADIUS and lon_delta <= GEofence_RADIUS:
        return "SAFE_ZONE"
    return "UNTRUSTED_ZONE"

# 2. Network Monitoring Engine
def scan_network_activity(zone):
    """Adjusts scanning port telemetry depending on location status."""
    # Standard ports to check for background sockets
    ports_to_audit = [80, 443, 8080, 9090] 
    print(f"\n[Audit] Status: {zone} | Initializing packet handshake analysis...")
    
    for port in ports_to_audit:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        # Scan local loopback interface for listening services
        result = s.connect_ex(('127.0.0.1', port)) 
        
        if result == 0:
            print(f"  [ALERT] Port {port} is OPEN active listening status.")
            if zone == "UNTRUSTED_ZONE":
                print(f"  [CRITICAL ALERT] Unauthorized background listener active in public sector!")
        else:
            if zone == "UNTRUSTED_ZONE":
                print(f"  [PASSIVE] Port {port} secure.")
        s.close()

# 3. Execution Control Loop
print("=[ Sentinel Integrated Geofence & Network Monitor Active ]=")
try:
    while True:
        current_lat, current_lon = get_current_location()
        zone_status = check_geofence(current_lat, current_lon)
        
        scan_network_activity(zone_status)
        
        # Idle delay to protect API throttling and processor states
        time.sleep(10) 
except KeyboardInterrupt:
    print("\n[INFO] Sentinel Monitoring Loop deactivated gracefully.")
