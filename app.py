import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=".env")
API_VERSION = os.getenv("LINODE_API_VERSION")
DOMAIN_NAME = os.getenv("DOMAIN_NAME")
LINODE_API_KEY = os.getenv("LINODE_API_KEY")
DNS_RECORD_ID = os.getenv("DNS_RECORD_ID")

# Debugging: Check if the environment variables are loaded
print(f"API Version: {API_VERSION}")
print(f"Linode API Key: {LINODE_API_KEY}")
print(f"Domain Name: {DOMAIN_NAME}")
print(f"DNS Record ID: {DNS_RECORD_ID}")

# Fetch the public IP from ipify
def get_public_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    if response.status_code == 200:
        ip_data = response.json()
        return ip_data.get("ip")
    else:
        print("Failed to retrieve public IP")
        return None

# Update DNS record on Linode
def update_dns_record(my_public_ip):
    # Determine if the IP is IPv6 or IPv4 and set the record type accordingly
    ip_type = "AAAA" if ":" in my_public_ip else "A"

    api_key = os.getenv('LINODE_API_KEY')
    domain_name = os.getenv('DOMAIN_NAME')
    dns_record_id = os.getenv('DNS_RECORD_ID')

    if not api_key or not domain_name or not dns_record_id:
        print("Missing necessary environment variables.")
        return

    # Define the Linode API endpoint
    url = f"https://api.linode.com/{API_VERSION}/domains/{domain_name}/records/{dns_record_id}"

    # Headers for Linode API authentication
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {LINODE_API_KEY}"
    }

    # Payload to update the DNS record with the new IP address
    data = {
        "target": my_public_ip,
        "name": "ddns-test1.grhost.net",  # Modify this as needed
        "type": ip_type,  # Use "AAAA" for IPv6 and "A" for IPv4
        "ttl": 300
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("DNS record updated successfully!")
    else:
        print(f"Failed to update DNS record: {response.status_code} {response.text}")

# Main function to check IP and update DNS
def main():
    public_ip = get_public_ip()
    if public_ip:
        print(f"Public IP: {public_ip}")
        update_dns_record(public_ip)

if __name__ == '__main__':
    main()
