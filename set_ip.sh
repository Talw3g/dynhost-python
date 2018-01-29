#!/usr/bin/env bash

APPKEY=""
APPSECRET=""
CONSUMERKEY=""
ZONE=""
ID=""

NEWIP=$0

URL="https://eu.api.ovh.com/1.0/domain/zone/$ZONE/dynHost/record/$ID"
ACTION="PUT"

TS=`date +%s`

PREHASH=$APPSECRET"+"$CONSUMERKEY"+"$ACTION"+"$URL"++"$TS
HASH=`echo -n $PREHASH| sha1sum| awk -F' ' '{print $1}'`
SIGNATURE='$1$'$HASH

curl \
-v \
-X $ACTION \
-H "X-Ovh-Application:$APPKEY" \
-H "X-Ovh-Timestamp:$TS" \
-H "X-Ovh-Signature:$SIGNATURE" \
-H "X-Ovh-Consumer:$CONSUMERKEY" \
-d subDomain="dyntest" \
-d ip=$NEWIP \
$URL

