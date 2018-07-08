from __future__ import absolute_import, unicode_literals
from celery import Celery


app = Celery('sandbox',
             broker='amqp://localhost',
             backend='redis://localhost',
             include=['sandbox.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)


if __name__ == '__main__':
    app.start()
