# == TCP ==
# vagrant@tr:~$ curl 10.0.2.101:8000

# vagrant@tr:~$ sudo tcpdump -i eth1 host 10.0.2.101
# tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
# listening on eth1, link-type EN10MB (Ethernet), capture size 262144 bytes
# ^A^A^Ac^A^A23:51:33.531063 IP 10.0.2.1.48682 > 10.0.2.101.8000: Flags [S], seq 3553660036, win 29200, options [mss 1460,sackOK,TS val 22277526 ecr 0,nop,wscale 7], length 0
# 23:51:33.531366 IP 10.0.2.101.8000 > 10.0.2.1.48682: Flags [R.], seq 0, ack 3553660037, win 0, length 0
# 23:51:38.543176 ARP, Request who-has 10.0.2.101 tell 10.0.2.1, length 28
# 23:51:38.543399 ARP, Reply 10.0.2.101 is-at 00:50:56:b6:36:33 (oui Unknown), length 46
