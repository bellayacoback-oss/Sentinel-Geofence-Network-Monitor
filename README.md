# Sentinel Geofence & Network Monitor Suite

An automated, context-aware cybersecurity toolset designed for mobile endpoint security, local network auditing, and Data Loss Prevention (DLP). This suite dynamically monitors device environments to detect rogue networks and prevent sensitive data leakage.

## 🚀 Key Modules
* **Geofencing Awareness (`geofencing_awarebeness.py`):** Enforces security policies based on location changes.
* **Network Audit (`network neighbor.py`):** Audits local TCP ports programmatically to map out vulnerabilities.
* **Traffic Auditor (`traffic.auditing.py`):** Monitors network stream metrics for unexpected chatter.
* **Data Loss Prevention (`leakinginfocheck.py`):** Scans files for cleartext credentials and sensitive indicators.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Engines:** `socket`, `json`, `os`, `time`
* **Platform:** Developed and compiled entirely on Android via Pydroid 3 and Termux
