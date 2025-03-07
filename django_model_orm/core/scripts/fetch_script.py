from core import models
from django.db import connection

def run():

    # restaurants = models.Restaurant.objects.all()
    # print(restaurants)
    # print(connection.queries)

    # first_restaurant = models.Restaurant.objects.first()
    # print(first_restaurant)
    # print(connection.queries)

    # last_restaurant = models.Restaurant.objects.last()
    # print(last_restaurant)
    # print(connection.queries)

    # index_restaurant = models.Restaurant.objects.all()[0]

    count = models.Restaurant.objects.count()
    print(count)
