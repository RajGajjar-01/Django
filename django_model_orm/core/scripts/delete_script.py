from core import models
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User

def run():
    restaurant = models.Restaurant.objects.first()

    count, what_deleted = restaurant.delete()

    print(count)
    print(what_deleted)
    print(connection.queries)