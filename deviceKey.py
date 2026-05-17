import json

def investigate_json(file_path):
    print(f"--- Investigating: {file_path} ---")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            # Step 1: See the top-level keys
            print(f"Main categories found: {list(data.keys())}")
            
            # Step 2: Look for common Google Home keys
            # Often it's under 'structures' or 'home_graph'
            if 'structures' in data:
                print("\nFound 'structures'. Looking for devices inside...")
                for structure in data['structures']:
                    devices = structure.get('devices', [])
                    for d in devices:
                        print(f"Device: {d.get('name', 'Unnamed')} ({d.get('type', 'Unknown')})")
            
            elif 'devices' in data:
                print("\nFound 'devices' list directly:")
                for d in data['devices']:
                    print(f"Device: {d.get('name', 'Unnamed')}")
            
            else:
                print("\nCould not find a standard 'devices' key.")
                print("Showing first few lines of data to identify structure:")
                # This prints the first 500 characters so you can see the 'grammar'
                print(str(data)[:500] + "...")

    except Exception as e:
        print(f"Error: {e}")

# Use your specific path
target = '/sdcard/Download/6/Takeout/Home App/HomeApp.json'
investigate_json(target)
