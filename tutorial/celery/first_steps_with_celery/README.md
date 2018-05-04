# First Steps with Celery
http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

Celery is a task queue with batteries included.

## Application
The first thing you need is a Celery instance. We call this the Celery application or just app for short. As this instance is used as the entry-point for everything you want to do in Celery, like creating tasks and managing workers, it must be possible for other modules to import it.

"""
# tasks.py
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y
"""


## Running the Celery worker server
$ celery -A tasks worker --loglevel=info


## Calling the task
"""
from tasks import add
add.delay(4, 4)
"""

## Keeping Results
tasks.py => app = Celery('tasks', backend='rpc://', broker='pyamqp://')

"""
result = add.delay(4, 4)
result.ready() # ==> True/False
result.get(timeout=1) # ==> 8
"""

## Configuration
"""
# celeryconfig.py
broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/Los_Angeles'
enable_utc = True
"""


