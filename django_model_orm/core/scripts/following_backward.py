from core import models
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User

def run():
    restaurant = models.Restaurant.objects.first()

    # Without related_name field
    # print(restaurant.rating_set.all()) 

    # With related_name field
    print(restaurant.ratings.all())
