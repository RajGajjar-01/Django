from core import models
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User

def run():

    # restaurant = models.Restaurant.objects.first()
    # print(restaurant.name)
    # restaurant.name = 'Pajji da dhaba'
    # restaurant.save()

    # print(connection.queries)

    sale = models.Sale.objects.first()
    sale.datetime = timezone.now() - timezone.timedelta(hours=3)
    sale.save()

    print("Done updating")