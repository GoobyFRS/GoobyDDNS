import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file.
load_dotenv(dotenv_path=".env")
LINODE_API_VERSION = os.getenv("LINODE_API_VERSION")
LINODE_API_KEY = os.getenv("LINODE_API_KEY")
ROOT_DOMAIN_NAME_HR = os.getenv("ROOT_DOMAIN_NAME")
SUBDOMAIN_RECORD_ID = os.getenv("SUBDOMAIN_RECORD_ID")
DOMAIN_RECORD_ID = os.getenv("DOMAIN_RECORD_ID")

# Checking my WAN IPv4 address using ipify.
def get_my_wan_ipv4():
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        my_public_ipv4 = response.json()
        return my_public_ipv4.get("ip")
    else:
        print("Failed to retrieve public IPv4 address.")
        return None

# Update DNS record on Linode
def update_dns_record(my_public_ip):
    LINODE_API_VERSION = os.getenv("LINODE_API_VERSION")
    LINODE_API_KEY = os.getenv("LINODE_API_KEY")
    SUBDOMAIN_RECORD_ID = os.getenv("SUBDOMAIN_RECORD_ID")
    DOMAIN_RECORD_ID = os.getenv("DOMAIN_RECORD_ID")
    # Basic IP Version checking. Currently is not used as the result will always result in an A record.
    ipv_type = "AAAA" if ":" in my_public_ip else "A"
    # Ensure all required variables load before sending a webhook.
    if not LINODE_API_VERSION or not LINODE_API_KEY or not DOMAIN_RECORD_ID or not SUBDOMAIN_RECORD_ID:
        print("Missing necessary environment variables.")
        return

    # Linode API Endpoint
    # https://techdocs.akamai.com/linode-api/reference/api-summary
    url = f"https://api.linode.com/{LINODE_API_VERSION}/domains/{DOMAIN_RECORD_ID}/records/{SUBDOMAIN_RECORD_ID}"

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
        "type": ipv_type,  # Use "AAAA" for IPv6 and "A" for IPv4
        "ttl": 300
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("DNS record updated successfully!")
    else:
        print(f"Failed to update DNS record: {response.status_code} {response.text}")

# Main function to check IP and update DNS
def main():
    my_public_ipv4 = get_my_wan_ipv4()
    if my_public_ipv4:
        print(f"Public IP: {my_public_ipv4}")
        update_dns_record(my_public_ipv4)

if __name__ == '__main__':
    main()
