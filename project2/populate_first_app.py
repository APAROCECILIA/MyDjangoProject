# Import necessary modules
import random
import os
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project2.settings')
import django
django.setup()

# Import Django models
from app2.models import webPage, AccessRecords, Topic

# Create an instance of Faker
fakegen = Faker()

# Define topics
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

# Function to add a topic
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

# Function to populate data
def populate(N=5):
    for entry in range(N):
        # Get topic for entry
        top = add_topic()
        
        # Create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        # Create the new webpage entry
        webpg = webPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        
        # Create the new access record entry
        acc_rec = AccessRecords.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")