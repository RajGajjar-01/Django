# March 13 2025

from core import models
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from django.db.models.functions import Upper, Length, Concat
from django.db.models import F, Count, Q
from pprint import pprint
from django.utils import timezone
import random

def run():
    # it =  models.Restaurant.TypeChoices.ITALIAN
    # mex = models.Restaurant.TypeChoices.MEXICAN

    # print(models.Restaurant.objects.filter(
    #     Q(restaurant_type=it) | Q(restaurant_type=mex)
    # ))

    # restaurants name contains either 'italian' or 'mexican'
    it_or_mex = Q(name__icontains='italian') | Q(name__icontains='mexican')
    # restaurants that are not recently opened
    not_recently_opened = Q(date_opened__gt = timezone.now() - timezone.timedelta(days=40))

    # res = models.Restaurant.objects.filter(it_or_mex | not_recently_opened)

    # for re in res:
    #     print(re)

    # res1 = models.Restaurant.objects.first()
    res2 = models.Restaurant.objects.last()

    # res1.capacity = 10
    # res2.capacity = 20

    # res1.save()
    # res2.save()

    # print(
    #     models.Restaurant.objects.filter(capacity__isnull=True).count()
    # )

    restaurants = models.Restaurant.objects.all()
    print(res2.sales.count())

    

    
    pprint(connection.queries)