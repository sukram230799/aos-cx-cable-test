# 🔌 AOS-CX 10/100 Mbit/s Cable Test

This repository contains example code for testing Ethernet cables connected to an AOS-CX switch, specifically to determine whether the cable is wired as 2-pair or 4-pair Ethernet.

The cable diagnostics feature of AOS-CX is used for this test.  
**⚠️ Note:** Running a test will **temporarily disconnect clients for approximately 7 seconds per port.**

In addition, this script demonstrates how to set the speed of an interface via the AOS-CX REST API.

> *Disclaimer:* This code is provided for illustrative and educational purposes only and is not an official Hewlett Packard Enterprise (HPE) product or supported solution. It is provided "as is," without warranty of any kind, express or implied. Use of this code is at your own risk. See the [LICENSE](./LICENSE) file for more information.

---

## 📘 About the AOS-CX API

This script utilizes the [AOS-CX REST API](https://developer.arubanetworks.com/aoscx/), which enables programmability and automation of Aruba switches.

Helpful links:

- 📚 [AOS-CX Developer Portal](https://developer.arubanetworks.com/aoscx/)
- 📖 [API Reference](https://developer.arubanetworks.com/aoscx/reference/)
- 🧭 [API Introduction](https://developer.arubanetworks.com/aoscx/docs/introduction)

---

## 🚀 Features

- Run cable diagnostics on switch ports
- Detect cable type: 2-pair vs. 4-pair
- Change port speed via REST API
- Works with AOS-CX switches supporting the diagnostics feature

---

## ⚠️ Warning

> Running the cable test will cause a **brief network disruption** (~7 seconds per port).  
> Please use with caution, especially in production environments.

---
