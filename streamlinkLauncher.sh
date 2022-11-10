#!/bin/sh
pid=$2

const="https://www.twitch.tv/"
req="$const$1"
streamlink -a "--file-caching=2000 --network-caching=2000" $req best
python3 maintk.pyw
