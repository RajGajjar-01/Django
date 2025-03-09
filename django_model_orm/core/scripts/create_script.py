from core import models
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User

def run():
    
    models.Restaurant.objects.create(
        name = 'Lapinoz Pizza',
        date_opened = timezone.now(),
        restaurant_type = models.Restaurant.TypeChoices.ITALIAN,
        longitude = 12.253519,
        latitude = 52.737683,
    )

    # print(connection.queries)

    # user = User.objects.first()
    # restaurant = models.Restaurant.objects.first()

    # models.Rating.objects.create(user = user, restaurant = restaurant, rating = 3)

    # models.Sale.objects.create(
    #     restaurant = models.Restaurant.objects.get(id=3),
    #     income = 425.00,
    #     datetime = timezone.now()
    # )

    user = models.User.objects.first()
    restaurant = models.Restaurant.objects.first()

    # method get_or_create() returns tuple [rating object, boolean created]
    rating, created = models.Rating.objects.get_or_create(
        restaurant = restaurant,
        user = user,
        rating = 4
    )

    if created:
        print("This will be printed if the rating object is created. created will be true")
    else :
        print("This will be printed if the rating object already exist. created will be false.")

    