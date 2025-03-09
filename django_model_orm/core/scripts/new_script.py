# Script March 8 2025

from core import models
from django.db import connection
import random

def run():
    staff, created = models.Staff.objects.get_or_create(name='John Wick')

    # # methods are add, remove, all, filter, set, clear, count

    # staff.restaurants.set(models.Restaurant.objects.all()[:10])

    # italian = staff.restaurants.filter(restaurant_type=models.Restaurant.TypeChoices.ITALIAN)

    # print(italian)

    # restaurant = models.Restaurant.objects.get(pk=9)

    # print(restaurant.staff_set.all())

    # restaurant = models.Restaurant.objects.first()
    # restaurant2 = models.Restaurant.objects.last()

    # models.StaffRestaurant.objects.create(
    #     staff = staff, restaurant = restaurant, salary = 28_000
    # )

    # models.StaffRestaurant.objects.create(
    #     staff = staff, restaurant = restaurant2, salary  = 34_000
    # )

    staff.restaurants.set(
        models.Restaurant.objects.all()[:10],
        through_defaults={'salary': random.randint(50_000, 80_000)}
    )