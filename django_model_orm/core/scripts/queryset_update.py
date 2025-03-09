from core import models
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User

def run():
    restaurants = models.Restaurant.objects.filter(name__contains = 'Pizza')

    print(restaurants)

    # This update method does not run save() method while updating and does not emit any signal eg. post_signal
    print(restaurants.update(
        date_opened = timezone.now(),
        website = 'https://test.com',
    ))

    print(connection.queries)