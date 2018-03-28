== Permanant change ==
https://success.docker.com/article/how-do-i-configure-the-default-bridge-docker0-network-for-docker-engine-to-a-different-subnet

$ cat /etc/docker/daemon.json
{
  "bip": "172.26.0.1/16"
}

$ sudo service docker restart

$ ifconfig docker0

$ docker run -it --rm <DOCKER_CONTAINER>
(docker) $ ip add show eth0
38: eth0@if39: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:c0:a8:64:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 192.168.100.2/24 scope global eth0
    ...


== Temp solution till reboot ==

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
