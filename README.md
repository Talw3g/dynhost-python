Simple python3 script to update OVH dynHost records.

## Open API access:

To create API credentials:
https://eu.api.ovh.com/createToken/

You need to grant the following rights :
 - **GET** on */domain/zone/$ZONE/dynHost/record* (to list the Dynhost ids)
 - **PUT** on */domain/zone/$ZONE/dynHost/record/**
 - **POST** on */domain/zone/$YOURBASEDOMAIN/refresh*

$ZONE is usually your base domain

The easiest (but more permissive) way is to set all rights on domain/zone/*

## Usage:

 1. Create a python3 venv under a folder "ovh" at the root of the repo.
 2. Activate the venv and run 'python3 -m pip install -U pip ovh'.
 3. Copy *ovh.conf.example* to *ovh.conf* and fill the info with the API credentials created above. Limit the read access of this file, as it contains sensitive data.
 4. Copy *config.py.example* to *config.py* and edit the "zone" and "subdomain" variables.
 5. Run *set_ip.py* as root.
