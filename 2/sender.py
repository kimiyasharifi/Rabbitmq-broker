import  pika


#create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#create channel
ch = connection.channel()

ch.queue_declare(queue='first', durable=True) #durable=true ---> queues are persisted to disk (related to only queue in channels)
message = "this is testing message"

ch.basic_publish(exchange='', routing_key='first', body=message, properties=pika.BasicProperties(delivery_mode=2, headers={'name':"kimia sharifi"}))     # sending another properties with message

print('sent message')
connection.close()