# GoobyDDNS

Creating a DDNS client is some sorta, "right of passage" kind of thing. There are stable, documented options available. But why not make my own? Thus we have Goobs Dynamic DNS Client for Akamai/Linode.

**Current Version:** 1.0.0

## Production Deployment - Linux

```shell
cd /your/desired/path/
git clone https://github.com/GoobyFRS/GoobyDDNS.git
chmod +x app.py
touch .env
```

Update the dotenv file with proper values. Be sure to update the ```.sh``` file with the proper path to this cloned repo.

```shell
crontab -e
*/15 * * * * /path/to/your/script/update_ddns.sh
```

### Project Development Setup - Windows

```txt
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

#### DOTENV File Example

```txt
LINODE_API_KEY=your_api_key
LINODE_API_VERSION=v4
ROOT_DOMAIN_NAME_HR=example.org
SUBDOMAIN_RECORD_ID=0123uuid
DOMAIN_RECORD_ID=4567uuid
FQDN=ddns.example.org
```
