# Wi-Fi Profile and Network Scanner

This Python script retrieves and displays information about previously connected Wi-Fi profiles, their passwords, and nearby Wi-Fi networks, including their passwords if available. It utilizes the `netsh` command available in Windows environments.

## Features

- **List Saved Wi-Fi Profiles:** Retrieves all Wi-Fi profiles saved on the system.
- **Retrieve Wi-Fi Passwords:** Extracts the password for each saved Wi-Fi profile.
- **Scan Nearby Networks:** Lists nearby Wi-Fi networks and their BSSIDs.
- **Show Network Passwords:** Displays the password for nearby networks if it matches one of the saved profiles.

## Requirements

- Python 3.x
- Windows OS (as `netsh` is specific to Windows)

## Installation

1. Clone the repository or download the script.
   ```bash
   git clone https://github.com/msaShahid/wifi-profile-scanner.git
   cd wifi-profile-scanner
   ```

2. Ensure Python 3.x is installed on your system.

## Usage

1. Open a command prompt or terminal.

2. Navigate to the directory where the script is located.

3. Run the script:
   ```bash
   python wifi_scanner.py
   ```

4. The script will display:
   - Previously connected Wi-Fi profiles and their passwords.
   - Nearby Wi-Fi networks, their BSSIDs, and passwords if available.

## Example Output

```
Previously Connected Wi-Fi Profiles and Keys:
ProfileName1                  |  Password123
ProfileName2                  |  No password found

Nearby Wi-Fi Networks:
SSID1                        |  BSSID1                        |  Password123
SSID2                        |  BSSID2                        |  N/A
```

## Code Explanation

- **`get_wifi_profiles()`**: Retrieves a list of all saved Wi-Fi profiles on the system.
- **`get_profile_key(profile)`**: Retrieves the password for a given Wi-Fi profile.
- **`get_nearby_networks(profiles)`**: Retrieves a list of nearby Wi-Fi networks and their BSSIDs, along with passwords if available.
- **`main()`**: Displays the list of saved Wi-Fi profiles with passwords and nearby networks with their BSSIDs and passwords.

## Troubleshooting

- Ensure you have the necessary permissions to run the script, as it requires access to system Wi-Fi settings.
- Ensure `netsh` is available and functioning on your system.

## Acknowledgements

- The script relies on the `netsh` command, which is part of the Windows operating system.

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have improvements. 

