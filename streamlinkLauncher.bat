

set "in=%1"
set "fileCache=%2"
set "netCache=%3"

:A

set "const=twitch.tv/"
set "req=%const%%in%"

streamlink -a "--file-caching=%fileCache% --network-caching=%netCache%" %req% best


python maintk.pyw