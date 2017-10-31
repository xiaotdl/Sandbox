https://www.rabbitmq.com/install-debian.html

# add the APT repository to your /etc/apt/sources.list.d:
$ sudo sh -c "echo 'deb http://www.rabbitmq.com/debian/ testing main' >> /etc/apt/sources.list.d/rabbitmq.list"

# add our public key to your trusted key list using apt-key(8):
$ wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

$ sudo apt-get update
$ sudo apt-get install rabbitmq-server

# start the server
$ sudo service rabbitmq-server start
 * Starting message broker rabbitmq-server
    ...done.

# monitor log
$ tailf /var/log/rabbitmq/rabbit@trusty64.log
