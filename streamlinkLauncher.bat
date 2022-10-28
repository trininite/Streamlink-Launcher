@echo off


set "in=%1"

:A

set "const=twitch.tv/"
set "req=%const%%in%"

streamlink -a "--file-caching=2000 --network-caching=2000" %req% best


python maintk.pyw