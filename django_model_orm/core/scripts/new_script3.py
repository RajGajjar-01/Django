# Script March 9 2025

from core import models
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from django.db.models.functions import Upper, Length, Concat
from django.db.models import Count, Avg, Min, Max, Sum, StdDev, Variance, CharField, Value
from pprint import pprint
from django.utils import timezone

def run():
    # Get number of ratings and avg_rating of all restaurants along with their names

    # restaurants = models.Restaurant.objects.annotate(
    #     num_of_ratings = Count('ratings__rating'),
    #     avg_rating = Avg('ratings__rating')
    # )

    # print(restaurants.values('name', 'num_of_ratings', 'avg_rating'))


    # Get no_of_ratings as per restaurant type ---> Read docs here for this
    restaurants = models.Restaurant.objects.values('restaurant_type').annotate(
        num_ratings=Count('ratings')
    )
    print(restaurants)