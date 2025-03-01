import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the public IP from ipify
def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        ip_data = response.json()
        return ip_data.get("ip")
    else:
        print("Failed to retrieve public IP")
        return None

# Update DNS record on Linode
def update_dns_record(public_ip):
    api_key = os.getenv('LINODE_API_KEY')
    domain_name = os.getenv('DOMAIN_NAME')
    dns_record_id = os.getenv('DNS_RECORD_ID')

    if not api_key or not domain_name or not dns_record_id:
        print("Missing necessary environment variables.")
        return

    # Define the Linode API endpoint
    url = f'https://api.linode.com/v4/domains/{domain_name}/records/{dns_record_id}'

    # Headers for Linode API authentication
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    # Payload to update the DNS record with the new IP address
    data = {
        "target": public_ip,
        "name": "www",  # You can modify this for a subdomain
        "type": "A",
        "ttl": 300
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("DNS record updated successfully!")
    else:
        print(f"Failed to update DNS record: {response.text}")

# Main function to check IP and update DNS
def main():
    public_ip = get_public_ip()
    if public_ip:
        print(f"Public IP: {public_ip}")
        update_dns_record(public_ip)

if __name__ == '__main__':
    main()
