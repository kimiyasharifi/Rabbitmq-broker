import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f'Received {body}')

ch.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('waiting for message, to exit')

ch.start_consuming()