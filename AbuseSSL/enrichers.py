import requests
import whois
from models import IP
import collectors
import whois
#add_some_whois_information

#Virus Total enrichment 
ip_address='217.197.107.204'
#relationship with samples
api_key = '40bcedcfadeb59b04dea13b934543d386c1c79106b3344be5ed9106c887231e7'
# Correct the URL format for the VirusTotal API request

url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}/communicating_files?limit=10"

headers = {
    'accept': 'application/json',
    'x-apikey': api_key
}

response = requests.get(url, headers=headers)

print(response.text)
