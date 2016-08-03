# Ref:
# http://stackoverflow.com/questions/24792462/python-scapy-dns-sniffer-and-parser


from scapy.all import *
from datetime import datetime
import time
import datetime
import sys

############# MODIFY THIS PART IF NECESSARY ###############
interface = 'any'
filter_bpf = 'udp and port 53'

# ------ SELECT/FILTER MSGS
def select_DNS(pkt):
    pkt_time = pkt.sprintf('%sent.time%')
# ------ SELECT/FILTER DNS MSGS
    try:
        if DNSQR in pkt and pkt.dport == 53:
        # queries
           print '[**] Detected DNS QR Message at: ' + pkt_time

        elif DNSRR in pkt and pkt.sport == 53:
        # responses
           print '[**] Detected DNS RR Message at: ' + pkt_time

    except:
        pass
# ------ START SNIFFER
sniff(iface=interface, filter=filter_bpf, store=0,  prn=select_DNS)


# >>>
# $ nslookup www.facebook.com
# ...
# Address: 173.252.74.68

# >>>
# $ sudo python %
# WARNING: Failed to execute tcpdump. Check it is installed and in the PATH
# WARNING: No route found for IPv6 destination :: (no default route?)
# [**] Detected DNS QR Message at: 22:18:13.148480
# {'sent_time': 0, 'fields': {'src': '00:50:56:b7:f4:bc', 'dst': '00:1c:73:00:00:99', 'type': 2048}, 'aliastypes': [<class 'scapy.layers.l2.Ether'>], 'post_transforms': [], 'underlayer': None, 'fieldtype': {'src': <Field (Ether).src>, 'dst': <Field (Ether).dst>, 'type': <Field (Ether).type>}, 'time': 1470201493.148481, 'initialized': 1, 'overloaded_fields': {'type': 2048}, 'packetfields': [], 'payload': <IP  version=4L ihl=5L tos=0x0 len=62 id=53037 flags= frag=0L ttl=64 proto=udp chksum=0x596b src=10.192.10.141 dst=10.192.50.10 options=[] |<UDP  sport=40417 dport=domain len=42 chksum=0x5252 |<DNS  id=52332 qr=0L opcode=QUERY aa=0L tc=0L rd=1L ra=0L z=0L rcode=ok qdcount=1 ancount=0 nscount=0 arcount=0 qd=<DNSQR  qname='www.facebook.com.' qtype=A qclass=IN |> an=None ns=None ar=None |>>>, 'default_fields': {'src': None, 'dst': None, 'type': 0}}
# [**] Detected DNS RR Message at: 22:18:13.153814
# {'sent_time': 0, 'fields': {'src': '00:1c:73:87:3e:f2', 'dst': '00:50:56:b7:f4:bc', 'type': 2048}, 'aliastypes': [<class 'scapy.layers.l2.Ether'>], 'post_transforms': [], 'underlayer': None, 'fieldtype': {'src': <Field (Ether).src>, 'dst': <Field (Ether).dst>, 'type': <Field (Ether).type>}, 'time': 1470201493.153814, 'initialized': 1, 'overloaded_fields': {'type': 2048}, 'packetfields': [], 'payload': <IP  version=4L ihl=5L tos=0x0 len=107 id=15859 flags=DF frag=0L ttl=254 proto=udp chksum=0xec77 src=10.192.50.10 dst=10.192.10.141 options=[] |<UDP  sport=domain dport=40417 len=87 chksum=0xe510 |<DNS  id=52332 qr=1L opcode=QUERY aa=0L tc=0L rd=1L ra=1L z=0L rcode=ok qdcount=1 ancount=2 nscount=0 arcount=0 qd=<DNSQR  qname='www.facebook.com.' qtype=A qclass=IN |> an=<DNSRR  rrname='www.facebook.com.' type=CNAME rclass=IN ttl=1038 rdata='star-mini.c10r.facebook.com.' |<DNSRR  rrname='star-mini.c10r.facebook.com.' type=A rclass=IN ttl=41 rdata='173.252.74.68' |>> ns=None ar=None |>>>, 'default_fields': {'src': None, 'dst': None, 'type': 0}}
