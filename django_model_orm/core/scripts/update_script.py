from core import models
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User

def run():

    # restaurant = models.Restaurant.objects.first()
    # print(restaurant.name)
    # restaurant.name = 'Iyer da dhaba'

    # just to update name field we wttie update_fields attribut
    # restaurant.save(update_fields=['name']) 

    # print(connection.queries)

    # sale = models.Sale.objects.first()
    # sale.datetime = timezone.now() - timezone.timedelta(hours=3)
    # sale.save()

    print(models.Restaurant.objects.count())
    print(models.Rating.objects.count())
    print(models.Sale.objects.count())

    print("Done updating")