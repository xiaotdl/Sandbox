import json
from time import sleep
from tasks import add

if __name__ == '__main__':
    r = add.apply_async((1,2))
    print vars(r)

    while not r.ready():
        print 'waiting...'
        print 'r.status:', r.status
        print 'r.state:', r.state
        print 'r.info:', r.info
        sleep(0.1)

    print 'done!'
    print vars(r)
    print r.get()
    print 'r.status:', r.status
    print 'r.state:', r.state
    print 'r.info:', json.dumps(r.info, indent=4)

