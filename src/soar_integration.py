import requests

class SOARIntegration:
    def __init__(self, soar_url, api_key):
        self.soar_url = soar_url
        self.api_key = api_key

    def create_incident(self, email_details, threat_intel_results):
        incident_data = {
            'title': f"Phishing Email: {email_details['subject']}",
            'description': f"From: {email_details['from']}\n\nBody: {email_details['body']}",
            'threat_intel': threat_intel_results,
            'status': 'New'
        }
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(f"{self.soar_url}/incidents", json=incident_data, headers=headers)
        return response.json()