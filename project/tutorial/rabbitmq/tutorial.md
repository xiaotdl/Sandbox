# RabbitMQ Tutorial

## Part 1. Introduction
https://www.rabbitmq.com/tutorials/tutorial-one-python.html

RabbitMQ is **a message broker**: it accepts and forwards messages.

RabbitMQ, and messaging in general, uses some jargon.
**A producer** is a program that sends messages.
**Producing** means sending.
**A queue** is where messages store. A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer. Many producers can send messages that go to one queue, and many consumers can try to receive data from one queue.
**A consumer** is a program that mostly waits to receive messages.
**Consuming** means receiving.

Note that the producer, consumer, and broker do not have to reside on the same host; indeed in most applications they don't.

## Hello World!
(using the Pika Python client)
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.
The Advanced Message Queuing Protocol (AMQP) is an open standard application layer protocol for message-oriented middleware.
$ sudo pip install pika==0.11.0

It's a "Hello World" of messaging.
a producer (sender) that sends a single message,
a consumer (receiver) that receives messages and prints them out.

### Sending
Our first program send.py will send a single message to the queue.
The first thing we need to do is to establish a connection with RabbitMQ server.

### Receiving
Our second program receive.py will receive messages from the queue and print them on the screen.
Again, first we need to connect to RabbitMQ server. The code responsible for connecting to Rabbit is the same as previously.

list current queues:
$ sudo rabbitmqctl list_queues
Listing queues
hello   1

### Demo
(rabbitmq) vagrant@trusty64:~/.virtualenvs/rabbitmq/src$ python receive.py
 [] Waiting for messages. To exit press CTRL+C
 [x] Received 'Hello World!'
 [x] Received 'Hello World!'

(rabbitmq) vagrant@trusty64:~/.virtualenvs/rabbitmq/src$ python send.py
 [x] Sent 'Hello World!'


## Part 2. Work Queues
https://www.rabbitmq.com/tutorials/tutorial-two-python.html

In this part, we'll create a Work Queue that will be used to distribute _time-consuming tasks_ among _multiple workers_.

