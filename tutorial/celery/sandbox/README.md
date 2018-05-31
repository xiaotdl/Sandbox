## start message queueu (rabbitmq)
$ sudo apt-get install rabbitmq-server

## start backend datastore (redis)
Sandbox/tutorial/celery/flask_with_celery_based_bg_tasks/simple-example$
    ./run-redis.sh

## start worker (celery worker)
Sandbox/tutorial/celery$
    celery worker -A sandbox.tasks --loglevel=info

## schedule (celery client)
Sandbox/tutorial/celery$
    python -m sandbox.schedule
