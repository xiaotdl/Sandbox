#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# All we need to know now is how to use a default exchange identified by an empty string.
# This exchange is special - it allows us to specify exactly to which queue the message should go.
channel.basic_publish(exchange='',
                      routing_key='hello', # points to queue name
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
