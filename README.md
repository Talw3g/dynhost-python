Simple pure bash script to update OVH dynHost records.

To create API credentials:
https://eu.api.ovh.com/createToken/

You need to grant the following rights :
 - **GET** on */domain/zone/$ZONE/dynHost/record* (to list the Dynhost ids)
 - **PUT** on */domain/zone/$ZONE/dynHost/record/**
 - **POST** on */domain/zone/$YOURBASEDOMAIN/refresh*

$ZONE is usually your base domain

The easiest (but more permissive) way is to set all rights on domain/zone/*
