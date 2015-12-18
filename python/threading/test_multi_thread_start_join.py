import time
import urllib2


print "Single threaded way"
def get_responses():
    urls = ['http://www.google.com', 'http://www.amazon.com', 'http://www.ebay.com', 'http://www.alibaba.com', 'http://www.reddit.com']
    start = time.time()
    for url in urls:
        resp = urllib2.urlopen(url)
        print url, resp.getcode()
    print "Elapsed time: %s" % (time.time()-start)

get_responses()



print "Multi threaded way"
import threading

class GetUrlThread(threading.Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        resp = urllib2.urlopen(self.url)
        print self.url, resp.getcode()

def get_responses():
    urls = ['http://www.google.com', 'http://www.amazon.com', 'http://www.ebay.com', 'http://www.alibaba.com', 'http://www.reddit.com']
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "Elapsed time: %s" % (time.time()-start)

get_responses()
