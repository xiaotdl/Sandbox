import time
from worker.app import celery, db


@celery.task(bind=True)
def long_add(self, task_id, a, b):
    """Background task that runs a long add function."""
    print "Invoking long_add(%s, %s, %s, %s)" % (self, task_id, a, b)
    self.update_state(state='IN_PROGRESS')

    db.update_task_status(task_id, 'STARTED')
    db.add_task_msg(task_id, '[TestWorker] Started task %s...' % task_id)

    # executing task
    time.sleep(2)
    res = a + b

    db.update_task_status(task_id, 'COMPLETED')
    db.add_task_msg(task_id, '[TestWorker] Completed task %s...' % task_id)

    return {
        'sum': res
    }
