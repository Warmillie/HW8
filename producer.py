import pika
from mongoengine import connect
from faker import Faker
from models import Contact

credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='HW', exchange_type='direct')
channel.queue_declare(queue='HW_queue', durable=True)
channel.queue_bind(exchange='HW', queue='HW_queue')


connect(db='HW8', host='mongodb+srv://warmillie1:%23EDCxsw2!QAZ@cluster0.ezi9yvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


def generate_fake_contacts(num_contacts):
    fake = Faker()
    for _ in range(num_contacts):
        name = fake.name()
        email = fake.email()
        contact = Contact(full_name=name, email=email)
        contact.save()
        channel.basic_publish(exchange='', routing_key='HW_queue', body=str(contact.id))


if __name__ == '__main__':
    num_contacts = 10  
    generate_fake_contacts(num_contacts)
    print(f'{num_contacts} фейкових контактів було створено та відправлено у чергу.')
