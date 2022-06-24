#! ./ovh/bin/python3

import ovh, requests
import config
from time import localtime, strftime

print(strftime("%d/%m/%Y %H:%M:%S -----> ", localtime()), end="")

zone = config.zone
subdomain = config.subdomain

client = ovh.Client()

new_ip = requests.get('http://ipinfo.io/ip').content.decode("ascii")

ID = client.get(
    "/domain/zone/{:s}/dynHost/record".format(zone),
    subDomain=subdomain,
    )[0]

old_ip = client.get(
    "/domain/zone/{:s}/dynHost/record/{:d}".format(zone, ID)
    )['ip']

if old_ip != new_ip:
    client.put(
        "/domain/zone/{:s}/dynHost/record/{:d}".format(zone, ID),
        ip=new_ip,
    )
    client.post("/domain/zone/{:s}/refresh".format(zone))
    print("New IP set : ", new_ip)

else:
    print("No change")

