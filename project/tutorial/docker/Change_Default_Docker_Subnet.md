Ref: https://support.zenoss.com/hc/en-us/articles/203582809-How-to-Change-the-Default-Docker-Subnet

🍺 sudo systemctl stop serviced
Failed to stop serviced.service: Unit serviced.service not loaded.

🍺 sudo systemctl stop dockerd
Failed to stop dockerd.service: Unit dockerd.service not loaded.

🍺 sudo iptables -t nat -F POSTROUTING

🍺 sudo ip link set dev docker0 down

🍺 sudo ip addr del 172.17.42.1/16 dev docker0

🍺 sudo ip addr add 10.10.1.1/24 dev docker0

🍺 sudo ip link set dev docker0 up

🍺 ip addr show docker0
