#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Creating a queue using queue_declare is idempotent
# It's a good practice to repeat declaring the queue in both send and receive programs.
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# enter a never-ending loop that waits for data and runs callbacks whenever necessary.
channel.start_consuming()
