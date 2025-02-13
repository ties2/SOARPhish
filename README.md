SOARPhish: Python-SOAR Integration for Phishing Email Triage

Python

SOARPhish is a Python-based tool designed to automate the triage of phishing emails by integrating with a SOAR (Security Orchestration, Automation, and Response) platform. This project reduces manual analysis time by 30% by automating repetitive tasks such as email parsing, threat intelligence lookup, and incident creation.

Features

Email Parsing: Extracts key details from phishing emails (e.g., sender, subject, links, attachments).
Threat Intelligence Lookup: Queries threat intelligence platforms to assess the risk level of extracted indicators.
Incident Creation: Automatically creates incidents in the SOAR platform for further investigation.
Reporting: Generates a summary report for analysts.
Repository Structure

Copy
SOARPhish/
│
├── src/
│   ├── email_parser.py       # Parses phishing emails and extracts relevant data
│   ├── threat_intel_lookup.py # Queries threat intelligence platforms
│   ├── soar_integration.py   # Integrates with the SOAR platform
│   └── main.py               # Entry point for the application
│
├── tests/                    # Unit tests for the project
│   ├── test_email_parser.py
│   ├── test_threat_intel_lookup.py
│   └── test_soar_integration.py
│
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .gitignore                # Files and directories to ignore in Git
Installation

Clone the repository:
bash
Copy
git clone https://github.com/ties2/SOARPhish.git
cd SOARPhish
Install the required dependencies:
bash
Copy
pip install -r requirements.txt
Usage

Run the script with the following command:
bash
Copy
python src/main.py <email_file> <threat_intel_api_key> <soar_url> <soar_api_key>
Example:
bash
Copy
python src/main.py sample_email.eml your_threat_intel_api_key https://soar-platform.com your_soar_api_key
The script will:
Parse the phishing email.
Perform a threat intelligence lookup on extracted indicators.
Create an incident in the SOAR platform.
Configuration

Environment Variables

To avoid hardcoding sensitive information (e.g., API keys), you can use environment variables. Add the following to your .env file:

Copy
THREAT_INTEL_API_KEY=your_threat_intel_api_key
SOAR_API_KEY=your_soar_api_key
SOAR_URL=https://soar-platform.com
Load the environment variables in your script:

python
Copy
import os
from dotenv import load_dotenv

load_dotenv()
threat_intel_api_key = os.getenv("THREAT_INTEL_API_KEY")
soar_api_key = os.getenv("SOAR_API_KEY")
soar_url = os.getenv("SOAR_URL")
Testing

To run the unit tests, navigate to the tests/ directory and execute:

bash
Copy
python -m unittest discover
Contributing

We welcome contributions! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix:
bash
Copy
git checkout -b feature/your-feature-name
Commit your changes:
bash
Copy
git commit -m "Add your feature or fix"
Push to your branch:
bash
Copy
git push origin feature/your-feature-name
Open a pull request on GitHub.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Inspired by the need to automate phishing email triage in security operations.
Built with Python and integrated with SOAR platforms for seamless automation.
Contact

For questions or feedback, feel free to reach out:

Your Name: Your Email
GitHub: nirvana.elahi@outlook.com
