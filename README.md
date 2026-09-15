<div align="center">

<pre align="center">
███╗   ███╗ ██████╗      ██╗ ██████╗     ██████╗  █████╗ ████████╗
████╗ ████║██╔═══██╗     ██║██╔═══██╗    ██╔══██╗██╔══██╗╚══██╔══╝
██╔████╔██║██║   ██║     ██║██║   ██║    ██████╔╝███████║   ██║   
██║╚██╔╝██║██║   ██║██   ██║██║   ██║    ██╔══██╗██╔══██║   ██║   
██║ ╚═╝ ██║╚██████╔╝╚█████╔╝╚██████╔╝    ██║  ██║██║  ██║   ██║   
╚═╝     ╚═╝ ╚═════╝  ╚════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
</pre>

# Mojo RAT

**Android Device Management & Security Audit Tool**

[![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS%20%7C%20Termux-lightgrey?style=for-the-badge)](https://github.com/mojoolabs/Mojo-RAT)
[![ADB](https://img.shields.io/badge/Requires-ADB-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://developer.android.com/tools/adb)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](./LICENSE)

</div>

---

## Overview

Mojo RAT is a Python tool built on **ADB (Android Debug Bridge)** that provides an interactive terminal menu to manage, monitor, and audit Android devices from a PC — over USB or Wi-Fi, with no companion app required on the phone.

> **For authorized use only.** Use exclusively on devices you own or have explicit written permission to access.

## License Key

On first launch the tool prompts for a license key. Use:

```
FIREWALLBREAKER
```

## Features

- **Device control** — info, connect/disconnect (USB & Wi-Fi), reboot, power off, storage, connection history.
- **Screen & media** — screenshot, screen recording, live mirroring (`scrcpy`), remote camera capture.
- **Apps** — list/install/uninstall APKs, launch apps.
- **Files & data** — push/pull files, dump contacts, send SMS, pull `logcat`.
- **Security audit (Option 22)** — root detection, permission auditing, patch/encryption checks, debuggable-app scan, interactive shell, network checks (`nmap`, `netstat`), SMS/call-log export, vulnerability scan.

## Requirements

| Dependency | Required | Purpose |
|------------|----------|---------|
| Python 3.7+ | Yes | Runtime |
| colorama | Yes | Terminal colors (`pip install -r requirements.txt`) |
| ADB | Yes | Device communication |
| scrcpy | Optional | Screen mirroring (not available in Termux) |
| nmap | Optional | Network scanning |

## Installation

| Platform | Command |
|----------|---------|
| Ubuntu / Debian / Kali | `sudo apt install -y python3 adb scrcpy git && git clone https://github.com/mojoolabs/Mojo-RAT.git && cd Mojo-RAT && pip3 install -r requirements.txt && python3 mojo_rat_v1.3.py` |
| Arch / Manjaro | `sudo pacman -S python android-tools scrcpy git && git clone https://github.com/mojoolabs/Mojo-RAT.git && cd Mojo-RAT && pip install -r requirements.txt && python3 mojo_rat_v1.3.py` |
| macOS | `brew install python android-platform-tools scrcpy git && git clone https://github.com/mojoolabs/Mojo-RAT.git && cd Mojo-RAT && pip3 install -r requirements.txt && python3 mojo_rat_v1.3.py` |
| Windows | Install Python + ADB (add both to PATH), then: `git clone https://github.com/mojoolabs/Mojo-RAT.git && cd Mojo-RAT && pip install -r requirements.txt && python mojo_rat_v1.3.py` |
| Termux | `pkg install python git android-tools && git clone https://github.com/mojoolabs/Mojo-RAT.git && cd Mojo-RAT && pip install -r requirements.txt && python mojo_rat_v1.3.py` |

## Usage

```bash
python3 mojo_rat_v1.3.py   # latest (use `python` on Windows)
```

| File | Version |
|------|---------|
| `mojo_rat_v1.3.py` | Latest — full menu + security audit suite |
| `mojo_rat_v1.2.py` | 20-option menu |
| `mojo_rat_v1.1.py` | Core device/screen features |

Output files (screenshots, recordings, logs, dumps) are written to the directory you run the script from.
