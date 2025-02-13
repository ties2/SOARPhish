# SOARPhish: Python-SOAR Integration for Phishing Email Triage

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

   Clone the repository:
   ```bash
   git clone https://github.com/ties2/SOARPhish.git
   cd SOARPhish



   Run the script:
   ```bash
   python src/main.py sample_email.eml your_threat_intel_api_key https://soar-platform.com your_soar_api_key


   Example Input

Email file: sample_email.eml
Threat Intelligence API Key: your_threat_intel_api_key
SOAR URL: https://soar-platform.com
SOAR API Key: your_soar_api_key
Example Output

1. Parsed Email Details

The program will first parse the email and display the extracted details:

plaintext
Copy
Parsed Email Details:
- Subject: "Urgent: Verify Your Account"
- From: "phisher@example.com"
- To: "user@example.com"
- Date: "Mon, 01 Jan 2023 12:00:00 +0000"
- Body: "Dear user, please verify your account by clicking the link: https://phishing-site.com"
- Attachments: []
- Links: ["https://phishing-site.com"]
2. Threat Intelligence Lookup Results

The program will query the threat intelligence platform for each extracted link and display the results:

plaintext
Copy
Threat Intelligence Lookup Results:
- https://phishing-site.com: {"reputation": "malicious", "confidence": 95}
3. SOAR Incident Creation

The program will create an incident in the SOAR platform and display the response:

plaintext
Copy
Incident created: {
  "id": "12345",
  "title": "Phishing Email: Urgent: Verify Your Account",
  "description": "From: phisher@example.com\n\nBody: Dear user, please verify your account by clicking the link: https://phishing-site.com",
  "threat_intel": {
    "https://phishing-site.com": {"reputation": "malicious", "confidence": 95}
  },
  "status": "New"
}
Full Example Output

Here’s what the full output might look like when running the program:

plaintext
Copy
$ python src/main.py sample_email.eml your_threat_intel_api_key https://soar-platform.com your_soar_api_key

Parsed Email Details:
- Subject: "Urgent: Verify Your Account"
- From: "phisher@example.com"
- To: "user@example.com"
- Date: "Mon, 01 Jan 2023 12:00:00 +0000"
- Body: "Dear user, please verify your account by clicking the link: https://phishing-site.com"
- Attachments: []
- Links: ["https://phishing-site.com"]

Threat Intelligence Lookup Results:
- https://phishing-site.com: {"reputation": "malicious", "confidence": 95}

Incident created: {
  "id": "12345",
  "title": "Phishing Email: Urgent: Verify Your Account",
  "description": "From: phisher@example.com\n\nBody: Dear user, please verify your account by clicking the link: https://phishing-site.com",
  "threat_intel": {
    "https://phishing-site.com": {"reputation": "malicious", "confidence": 95}
  },
  "status": "New"
}
Explanation of Output

Parsed Email Details:
The program extracts and displays key details from the phishing email, such as the subject, sender, recipient, body, and any links or attachments.
Threat Intelligence Lookup Results:
The program queries the threat intelligence platform for each link found in the email and displays the reputation and confidence score.
SOAR Incident Creation:
The program creates an incident in the SOAR platform and displays the response, including the incident ID, title, description, threat intelligence results, and status.


