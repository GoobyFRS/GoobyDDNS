# GoobyDDNS

GoobyDDNS Linux Edition for Akamai/Linode.

**Current Version:** 1.0.0

## Production Deployment - Linux

**Step 1/3**

```shell
cd /your/desired/path/
git clone https://github.com/GoobyFRS/GoobyDDNS.git
chmod +x app.py
chmod +x update_ddns.sh
touch .env
source venv/bin/activate
pip install -r requirements.txt
python3 ./app.py
deactivate
```

**Step 2/3**

Update the dotenv file with proper values. Be sure to update the ```.sh``` file with the proper path to this cloned repo.

**Step 3/3**

```shell
crontab -e
*/15 * * * * /path/to/your/script/update_ddns.sh
```

### Project Development Setup - Windows

Windows Users should consider [GoobyDDNS_Winows]().

```txt
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
'''

#### DOTENV File Example

```txt
LINODE_API_KEY=your_api_key
LINODE_API_VERSION=v4
ROOT_DOMAIN_NAME_HR=example.org
SUBDOMAIN_RECORD_ID=0123uuid
DOMAIN_RECORD_ID=4567uuid
FQDN=ddns.example.org
```

