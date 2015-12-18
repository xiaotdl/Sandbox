print('%10.2f s' % 154.520035)
print('%10.2f s' % 24169.204950)

print('[elapsed time for %-40s] %20.2f s' % ("auto accept collection assertion", 24169.204950))
print('[elapsed time for %-40s] %20.2f s' % ("auto accept", 5140.272141))
print('[elapsed time for %-40s] %20.2f s' % ("assert log on bigip", 1382.956028))
# >>>
#     154.52 s
#   24169.20 s
# [elapsed time for auto accept collection assertion        ]             24169.20 s
# [elapsed time for auto accept                             ]              5140.27 s
# [elapsed time for assert log on bigip                     ]              1382.96 s


import datetime
d = datetime.timedelta(milliseconds=2416900.204950)
print d.seconds, d.microseconds
# >>> 2416 900205


opt = {'address': '1.2.3.4', 'user':'xili'}
print "address=%(address)s user=%(user)s" % opt
# >>> address=1.2.3.4 user=xili
print "address=%(address)s" % opt
# >>> address=1.2.3.4address=1.2.3.4 user=xili


quoted = {'_priority': '10',
         'address': '1.2.3.4',
         'api': 'None',
         'auth': 'BASIC',
         'device': 'this_is_a_device',
         'login_ref': 'None',
         'password': 'pwd',
         'port': '443',
         'proto': 'https',
         'timeout': '90',
         'token': 'None',
         'username': 'usr'
}
url = "{0[proto]}://{0[username]}:{0[password]}@{0[address]}:{0[port]}".format(quoted)
print url
# >>> https://usr:pwd@1.2.3.4:443