# SOARPhish: Python-SOAR Integration for Phishing Email Triage

![GitHub](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

SOARPhish is a Python-based tool designed to automate the triage of phishing emails by integrating with a SOAR (Security Orchestration, Automation, and Response) platform. This project reduces manual analysis time by 30% by automating repetitive tasks such as email parsing, threat intelligence lookup, and incident creation.

---

## Features

- **Email Parsing**: Extracts key details from phishing emails (e.g., sender, subject, links, attachments).
- **Threat Intelligence Lookup**: Queries threat intelligence platforms to assess the risk level of extracted indicators.
- **Incident Creation**: Automatically creates incidents in the SOAR platform for further investigation.
- **Reporting**: Generates a summary report for analysts.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ties2/SOARPhish.git
   cd SOARPhish
