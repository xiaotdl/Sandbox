from __future__ import absolute_import, unicode_literals
from .celery import app
from time import sleep

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(bind=True)
def add(self, x, y):
    logger.info(('Executing add task id {0.id}, args: {0.args!r} '
                 'kwargs: {0.kwargs!r}').format(self.request))

    self.update_state(
        state='PROGRESS',
        meta={
        'current': 1,
        'total': 2,
        'status': 3}
    )

    sleep(1)
    # print task info
    return {
        'result': x + y,
        'self': str(self),
        'type-self': str(type(self)),
        'vars-self': str(vars(self)),
    }


@app.task
def mul(x, y):
    print("running mul...",x,y)
    sleep(1)
    return x * y


@app.task
def xsum(numbers):
    sleep(1)
    return sum(numbers)
