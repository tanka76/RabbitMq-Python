import os
import pika

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1",port="5672",credentials=pika.PlainCredentials('admin', 'password')))
channel = connection.channel()

def received_message(ch,method,properties,body):
    """
    What to do when a message is received..
    """
    print(f"Received Message is {body}")
    print("Processing the job")

    ## Acknowledge the message after processing
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Done")

queue_name='jobs'
# Declare the queue and create if it does not exist
channel.queue_declare(queue=queue_name)

# channel.basic_consume(queue=queue_name,on_message_callback=received_message,auto_ack=True)
channel.basic_consume(queue=queue_name,on_message_callback=received_message,auto_ack=False)

print(f"Waiting for messages in {queue_name}. To exit press Ctrl+C")
channel.start_consuming()



 