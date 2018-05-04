github: https://github.com/miguelgrinberg/flask-celery-example
blog: https://blog.miguelgrinberg.com/post/using-celery-with-flask

# start redis (serves as celery message broker + backend)
./run_redis.sh

# start celery workers (processes that run the bg jobs)
celery worker -A app.celery --loglevel=info

# start flask server (init celery client that issues bg jobs to celery worker)
python app.py

# run post_wait_task
python post_wait_task.py
