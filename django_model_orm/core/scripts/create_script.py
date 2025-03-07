from core import models
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User

def run():
    
    # models.Restaurant.objects.create(
    #     name = 'Pipo Pizza',
    #     date_opened = timezone.now(),
    #     restaurant_type = models.Restaurant.TypeChoices.ITALIAN,
    #     longitude = 12.253519,
    #     latitude = 52.737683,
    # )

    # print(connection.queries)

    user = User.objects.first()
    restaurant = models.Restaurant.objects.first()

    models.Rating.objects.create(user = user, restaurant = restaurant, rating = 3)


    