#!/usr/bin/osascript

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Toggle ClashX Proxy
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 
# @raycast.packageName Clash

# Documentation:
# @raycast.description Toggle ClashX Proxy
# @raycast.author Kuangye Chen
# @raycast.authorURL https://github.com/KuangyeChen

if application "ClashX" is running then
    tell application "ClashX" to toggleProxy
    log "Toggled ClashX Proxy"
else
    log "ClashX is not running"
end if
