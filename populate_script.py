import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from clients.models import Client

def creating_people(amount_people):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(amount_people):
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        tin = fake.random_number(digits=9)
        pin = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        cell = "{}{}".format(random.randint(2, 9), "".join(str(random.randint(0, 9)) for _ in range(8)))
        active = random.choice([True, False])
        p = Client(name=name, email=email, tin=tin, pin=pin, cell=cell, active=active)
        p.save()

creating_people(50)
print('success!')