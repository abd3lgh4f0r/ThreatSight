import requests
import whois
from models import IP
import collectors
import whois
#add_some_whois_information

#Virus Total enrichment 
ip_address='217.197.107.204'


import requests

def virus_total_enrichment_whois(ip):
    api_key = ''
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    headers = {
        'accept': 'application/json',
        'x-apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()

        # Extract WHOIS information if available
        whois_data = data.get('data', {}).get('attributes', {}).get('whois', 'No WHOIS data found')

        return whois_data
    else:
        return {"error": f"Failed to retrieve data: {response.status_code}"}



print(virus_total_enrichment_whois(ip_address))