import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

#FAKE POPULATION SCRIPT
from faker import Faker
from AppTwo.models import User

fakegen = Faker()

def add_user(N):
    for entry in range(N):
        fname = fakegen.first_name()
        lname = fakegen.last_name()
        fake_mail = fakegen.email()

        userDetail = User.objects.get_or_create(first_name=fname,last_name=lname,email=fake_mail)[0]

if __name__ == '__main__':
    print("Populating Script")
    add_user(20)
    print("Populating Complete")
