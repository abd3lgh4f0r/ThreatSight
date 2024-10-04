import requests
import csv
from io import StringIO
from models import IP

# URL of the SSL Blacklist CSV file
url = "https://sslbl.abuse.ch/blacklist/sslipblacklist.csv"

def fetch_blacklist_ips():
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Read the CSV data
        csv_content = response.text

        # Use StringIO to parse the CSV content
        csv_data = csv.reader(StringIO(csv_content))

       
        ip_data = []
        for row in csv_data:
            if row and not row[0].startswith("#"):  
                timestamp = row[0]
                ip_address = row[1]  
                port = row[2]       
                ip_data.append({"ip_address": ip_address, "time": timestamp, "port": port})

        return ip_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the blacklist: {e}")
        return []


def create_ip_objects(ip_data):
    
    ip_objects = []
    for entry in ip_data:
        ip_obj = IP(
            ip_address=entry.get('ip_address'),
            collected_at=entry.get('time'),
            port=entry.get('port')
            # Additional fields can be mapped here if available
        )
        ip_objects.append(ip_obj)
    
    return ip_objects



L=fetch_blacklist_ips()
obj=create_ip_objects(L)
print(obj[0].ip_address)