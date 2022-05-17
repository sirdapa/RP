import requests
import os
os.system("rm rp-master -Rf")
url = "https://gitlab.zam.io/wajinhakim/rp/-/archive/master/rp-master.tar.gz"
r = requests.get(url, allow_redirects=True, verify=False)
open('rp-master.tar.gz', 'wb').write(r.content)
os.system("tar xvf rp-master.tar.gz && rm rp-master.tar.gz")
