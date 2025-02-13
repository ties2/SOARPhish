import requests

class ThreatIntelLookup:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.threatintelplatform.com/v2/"

    def check_url_reputation(self, url):
        endpoint = f"{self.base_url}url/reputation"
        params = {'url': url, 'api_key': self.api_key}
        response = requests.get(endpoint, params=params)
        return response.json()

    def check_ip_reputation(self, ip):
        endpoint = f"{self.base_url}ip/reputation"
        params = {'ip': ip, 'api_key': self.api_key}
        response = requests.get(endpoint, params=params)
        return response.json()