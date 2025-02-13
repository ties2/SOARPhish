from src.email_parser import EmailParser
from src.threat_intel_lookup import ThreatIntelLookup
from src.soar_integration import SOARIntegration

def main(email_file, threat_intel_api_key, soar_url, soar_api_key):
    # Step 1: Parse the email
    parser = EmailParser(email_file)
    email_details = parser.parse_email()

    # Step 2: Perform threat intelligence lookup
    threat_intel = ThreatIntelLookup(threat_intel_api_key)
    threat_intel_results = {}
    for url in email_details['links']:
        threat_intel_results[url] = threat_intel.check_url_reputation(url)

    # Step 3: Create an incident in SOAR
    soar = SOARIntegration(soar_url, soar_api_key)
    incident_response = soar.create_incident(email_details, threat_intel_results)

    print(f"Incident created: {incident_response}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: python main.py <email_file> <threat_intel_api_key> <soar_url> <soar_api_key>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])