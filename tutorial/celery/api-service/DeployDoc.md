github: https://github.com/miguelgrinberg/flask-celery-example

blog: https://blog.miguelgrinberg.com/post/using-celery-with-flask

# start redis (result backend for celery)
```
./run_redis.sh
# modify redis.conf to bind 0.0.0.0

sudo apt install redis-tools

$ redis-cli
# disable protected-mode
127.0.0.1:6379> ping 
PONG
127.0.0.1:6379> client list
id=6 addr=127.0.0.1:57114 fd=8 name= age=3 idle=0 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=32768 obl=0 oll=0 omem=0 events=r cmd=client
127.0.0.1:6379> CONFIG GET protected-mode
1) "protected-mode"
2) "yes"
127.0.0.1:6379> CONFIG SET protected-mode no
OK
```

# start rabbitmq (message broker for celery)
```
apt-get install rabbitmq-server
rm ~/.erlang.cookie
service rabbitmq-server start

rabbitmqctl add_user admin admin
rabbitmqctl set_user_tags admin administrator
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
```

# start database
```
apt-get install python-dev libmysqlclient-dev

(for ubuntu15.04, download pkg.deb from https://launchpad.net/ubuntu/vivid/amd64/libmysqlclient-dev/5.6.28-0ubuntu0.15.04.1, then install it via: dpkg -i /path/to/pkg.deb)

pip install MySQL-python
```

```
# create database
mysql> CREATE DATABASE api_svr_db;
```

```
# allow remote access:
1) modify /etc/mysql/mysql.conf.d/mysqld.cnf to bind 0.0.0.0
$ sudo /etc/init.d/mysql restart

2) $ mysql -u<username> -p<pwd>
USER=worker
PASS=worker
mysql> use mysql;
mysql> CREATE user '<USER>'@'%' IDENTIFIED by '<PASS>';
mysql> GRANT ALL PRIVILEGES ON *.* TO '<USER>'@'%' WITH GRANT OPTION;
```

# start web server (schedule task to celery worker)
```
python wsgi.py
```

# deploy web server
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04

```
# Create the WSGI Entry Point
fit@apiserver-prod:~/git/api-service/api-server$
sudo vim wsgi.py

# Testing Gunicorn's Ability to Serve the Project
fit@apiserver-prod:~/git/api-service/api-server$
gunicorn --bind 0.0.0.0:5000 wsgi:app

# Create a systemd Unit File
sudo vim /etc/systemd/system/api-server.service
sudo systemctl start api-server
sudo systemctl enable api-server

# Configuring Nginx to Proxy Requests
sudo vim /etc/nginx/sites-available/api-server
sudo ln -s /etc/nginx/sites-available/api-server /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

# To reload after making changes
sudo systemctl restart api-server
```

# start celery workers (processes that run the bg jobs)
```
sudo apt install python-celery-common

celery worker -A worker.app -l info -Q code-coverage --concurrency=10 -n worker-cc-1@%h
```

# run scheduler
```
python schedule_task.py
```
