import time
import socket
import json

SAFE_ZONE_LAT = 49.1913
SAFE_ZONE_LON = -122.8490
GEofence_RADIUS = 0.005

def get_current_location():
    return 49.1913, -122.8490 

def check_geofence(lat, lon):
    lat_delta = abs(lat - SAFE_ZONE_LAT)
    lon_delta = abs(lon - SAFE_ZONE_LON)
    if lat_delta <= GEofence_RADIUS and lon_delta <= GEofence_RADIUS:
        return "SAFE_ZONE"
    return "UNTRUSTED_ZONE"

def scan_network_activity(zone):
    ports_to_audit = [80, 443, 8080, 9090] 
    print(f"\n[Audit] Status: {zone} | Initializing packet handshake analysis...")
    for port in ports_to_audit:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex(('127.0.0.1', port)) 
        if result == 0:
            print(f"  [ALERT] Port {port} is OPEN active listening status.")
        s.close()

print("=[ Sentinel Integrated Geofence & Network Monitor Active ]=")
try:
    while True:
        current_lat, current_lon = get_current_location()
        zone_status = check_geofence(current_lat, current_lon)
        scan_network_activity(zone_status)
        time.sleep(10) 
except KeyboardInterrupt:
    print("\n[INFO] Sentinel Deactivated.")
