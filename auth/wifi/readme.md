# 📡 P0X-WIFI AUDITOR v1.0
**Automated Wireless Security Auditing & Brute-Force Demonstration Tool**

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Category](https://img.shields.io/badge/Field-Cybersecurity-red?style=for-the-badge)

`P0X-WIFI AUDITOR` is a high-level Python framework designed to test the resilience of WPA2-PSK networks. By bridging the `pywifi` library with a custom combinatorial generator, it automates the discovery, profiling, and credential-testing phases of a wireless security audit.

---

## 🏗️ System Logic & Workflow

The auditor operates as a state machine, moving through three distinct phases: **Reconnaissance**, **Targeting**, and **Exhaustive Testing**.



### 1. Reconnaissance (Scanning)
The script communicates with the OS network stack to put the Wi-Fi card into a scan state. It captures beacon frames to extract:
* **SSID:** Service Set Identifier (Network Name).
* **BSSID:** The MAC address of the Access Point.
* **Signal Strength:** To prioritize networks with stable handshakes.

### 2. The Brute-Force Engine
Instead of loading static files, the script uses **Lexicographical Permutation**. It treats the password as a base-N number where N is the size of your character set.
* **Memory Footprint:** $O(1)$ — Only the current password exists in RAM at any given time.
* **Generator Logic:** `itertools.product` ensures no combinations are skipped or repeated.

---

## 🛠️ Installation & Configuration

### Prerequisites
* **Python 3.8+**
* **Admin/Sudo Privileges:** Required for low-level socket and interface control.
* **Requirements:**
  ```bash
  pip install pywifi