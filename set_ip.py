#! ./ovh/bin/python3

import ovh, requests
import config

zone = config.zone
subdomain = config.subdomain

client = ovh.Client()

IP = requests.get('http://ipinfo.io/ip').content.decode("ascii")

ids = client.get("/domain/zone/{:s}/dynHost/record".format(zone))

for ID in ids:
    dh = client.get("/domain/zone/{:s}/dynHost/record/{:d}".format(zone, ID))
    if dh["subDomain"] == subdomain:
        client.put("/domain/zone/{:s}/dynHost/record/{:d}".format(zone, ID), ip=IP)

client.post("/domain/zone/{:s}/refresh".format(zone))

