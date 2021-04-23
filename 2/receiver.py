import pika
import time


connection =pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = connection.channel()

ch.queue_declare(queue='first', durable=True)
print('waiting for message')


def callback(ch, method, properties, body):
    print(f'received {body}')
    print(method)
    # sending another properties with message
    print(properties.headers)
    time.sleep(6)
    print('Done!')
    #mannual ack 
    ch.basic_ack(delivery_tag=method.delivery_tag)


# for granular sent 
ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue='first', on_message_callback=callback)
ch.start_consuming()