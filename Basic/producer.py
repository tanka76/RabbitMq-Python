import os
import pika

# Establish a connection to RabbitMQ(TCP connection)
connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1",port="5672",credentials=pika.PlainCredentials('admin', 'password')))
channel = connection.channel()

channel.queue_declare(queue='jobs')
message="Hello From Producer !!!"
channel.basic_publish(exchange='', #use default exchange
                      routing_key='jobs', #queue name
                      body=message) #  message to be sent

print(f"{message} this is sent to queue")
connection.close()



 