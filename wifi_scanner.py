import subprocess

def get_wifi_profiles():
    """Retrieve a list of all saved Wi-Fi profiles."""
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1].strip() for i in data if "All User Profile" in i]
        return profiles
    except subprocess.CalledProcessError as e:
        print("Error fetching profiles:", e)
        return []

def get_profile_key(profile):
    """Retrieve the password for a given Wi-Fi profile."""
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        keys = [b.split(":")[1].strip() for b in results if "Key Content" in b]
        return keys[0] if keys else "No password found"
    except subprocess.CalledProcessError as e:
        print(f"Error fetching key for profile '{profile}' : ", e)
        return "Error retrieving password"

def get_nearby_networks(profiles):
    """Retrieve a list of nearby Wi-Fi networks and their BSSIDs, and passwords if available."""
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'network', 'mode=Bssid']).decode('utf-8', errors="backslashreplace").split('\n')
        networks = []
        ssid = None
        for line in data:
            line = line.strip()
            if line.startswith("SSID"):
                ssid = line.split(":")[1].strip()
            elif line.startswith("BSSID") and ssid:
                bssid = line.split(":")[1].strip()
                password = get_profile_key(ssid) if ssid in profiles else "N/A"
                networks.append((ssid, bssid, password))
            elif line == "":
                ssid = None   
        return networks
    except subprocess.CalledProcessError as e:
        print("Error fetching nearby networks : ", e)
        return []

def main():
    """Main function to display Wi-Fi profiles, their passwords, and nearby networks with passwords."""
    profiles = get_wifi_profiles()
    print("\n Previously Connected Wi-Fi Profiles and Keys : ")
    for profile in profiles:
        key = get_profile_key(profile)
        print("{:<30}|  {:<}".format(profile, key))
    

    networks = get_nearby_networks(profiles)
    print("\n Nearby Wi-Fi Networks : ")
    for ssid, bssid, password in networks:
        print("{:<30}|  {:<30}|  {:<}".format(ssid, bssid, password))

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
