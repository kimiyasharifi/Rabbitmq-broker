import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.queue_declare(queue='hello')

ch.basic_publish(exchange='', routing_key='hello', body='hello rabbitmq')
print('message sent')
connection.close()