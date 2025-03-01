# GoobyDDNS

Creating a DDNS client is some sorta, "right of passage" kind of thing. There are stable, documented options available. But why not make my own? Thus we have Goobs Dynamic DNS Client for Akamai/Linode.

**Current Version:** 0.0.1

## Project Setup - Windows

```txt
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

env

```txt
LINODE_API_KEY=your_api_key
LINODE_API_VERSION=v4
ROOT_DOMAIN_NAME_HR=example.org
SUBDOMAIN_RECORD_ID=0123uuid
DOMAIN_RECORD_ID=4567uuid
```
