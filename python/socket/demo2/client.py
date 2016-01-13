# Socket client example in python
# ref: http://www.binarytides.com/python-socket-programming-tutorial/
"""
Socket as a client:
    1. Create a socket
    2. (connect) Connect to remote server
    3. (sendall) Send some data
    4. (recv)    Receive a reply
    5. (close)   Close the socket
"""

import socket   # for sockets
import sys      # for exit

# == socket.connect() ==
try:
    # Create an AF_INET (IPv4), SOCK_STREAM (TCP) socket
    # Address Family : AF_INET (this is IP version 4 or IPv4)
    # Type           : SOCK_STREAM (this means connection oriented TCP protocol)
    #                  SOCK_DGRAM (which indicates non-connection UDP protocol, same as ICMP, ARP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print ('Failed to create socket:\n' +
           'Error code: %s\n' % msg[0] +
           'Error message: %s\n' % msg[1])
    sys.exit()
print 'Socket created successfully!'

host = 'www.google.com'
port = 80
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print "Hostname couldn't be resolved."
    sys.exit()
print 'Host %s is resolved into IP: %s' % (host, remote_ip)

# == socket.connect() ==
# Connect to remote server
server = (remote_ip, port)
sock.connect(server)
print 'Socket connected to %s:%s' % server

# == socket.sendall() ==
# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"
try:
    sock.sendall(message)
except socket.error:
    print 'Send failed!'
    sys.exit()
print 'Message sent successfully!'

# == socket.recv() ==
# Receive response from server
resp = sock.recv(4096)
print 'Response from server:\n', resp

# == socket.close() ==
# free up the socket
sock.close()

# >>>
# Socket created successfully!
# Host www.google.com is resolved into IP: 74.125.25.105
# Socket connected to 74.125.25.105:80
# Message sent successfully!
# Response from server:
# HTTP/1.1 200 OK
# Date: Wed, 13 Jan 2016 07:39:11 GMT
# Expires: -1
# Cache-Control: private, max-age=0
# Content-Type: text/html; charset=ISO-8859-1
# P3P: CP="This is not a P3P policy! See https://www.google.com/support/accounts/answer/151657?hl=en for more info."
# Server: gws
# X-XSS-Protection: 1; mode=block
# X-Frame-Options: SAMEORIGIN
# Set-Cookie: NID=75=v1oLWkYvAMct7K_2HUZ50hKSqAQPTkw8z154GIkVypyJOkdBdskx9AkivxzRsWEcyomu6B2wguplvLyODuZPobaPhRdJ4cRUDCPlNjB_5OeyAXqNUB0dVrAYcjXwDPvRR3SGtC1JzneN7Rk; expires=Thu, 14-Jul-2016 07:39:11 GMT; path=/; domain=.google.com; HttpOnly
# Accept-Ranges: none
# Vary: Accept-Encoding
# Transfer-Encoding: chunked

# 8000
# <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"><meta content="noodp" name="robots"><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script>(function(){window.google={kEI:'H_-VVtGiKY6ajwOorbP4Dg',kEXPI:'1350255,3700306,3700385,4028790,4029815,4031109,4032678,4033307,4036527,4038012,4039268,4042783,4042791,4043397,4043492,4044606,4044954,4045840,4046304,4046400,4048595,4048854,4048881,4050780,4050912,4050915,4050980,4051154,4051833,4054037,4054284,4054513,4055217,4055352,4055381,4055390,4055496,4055754,4055757,4055996,4056034,4056038,4056128,4056247,4056438,4056486,4056523,4057139,4057169,4057184,4057378,4057410,4057552,4057784,4057859,8300095,8300272,8300289,8300327,8500572,8502095,8502315,8502451,8502691,8502786,8502849,8502888,8502986,10200083,10201288,10201554,10201587',authuser:0,kscs:'c9c918f0_24'};google.kHL='en';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.wl=function(a,b){try{google.ml(Error(a),!1,b)}catch(d){}};google.time=function(){return(new Date).getTime()};google.log=function(a,b,d,e,g){a=google.logUrl(a,b,d,e,g);if(""!=a){b=new Image;var c=google.lc,f=google.li;c[f]=b;b.onerror=b.onload=b.onabort=function(){delete c[f]};window.google&&window.google.vel&&window.google.vel.lu&&window.google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,d,e,g){var c="",f=google.ls||"";if(!d&&-1==b.search("&ei=")){var h=google.getEI(e)}}})
