# Script March 9 2025 --> Django F() Object in Django Models

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
   # rating = models.Rating.objects.filter(rating=3).first()
   # rating.rating += 1
   # rating.save(update_fields=['rating']) 

   # Another way
   # rating = models.Rating.objects.filter(rating=4).first()
   # rating.rating = F('rating') + 1
   # rating.save()


   # Making ratings from 5 stars to 10 stars
   # models.Rating.objects.update(rating=F('rating')*2)
   # models.Rating.objects.update(rating=F('rating')/2)

   # Another way  of doing the above is to bring each rating instance in python and then making changes


   # F() expression to calculate profit and loss
   # sales = models.Sale.objects.all()

   # for sale in sales:
   #    sale.expenditure = random.uniform(5, 100)
   
   # models.Sale.objects.bulk_update(sales, ['expenditure'])

   # sales = models.Sale.objects.annotate(profit = F('income') - F('expenditure')).order_by('profit')
   # for sale in sales:
   #    print(sale.profit)

   # sales = models.Sale.objects.filter(income__gte=F('expenditure')).count()
   # sales = models.Sale.objects.filter(income__lte=F('expenditure')).count() 

   # sales = models.Sale.objects.aggregate(
   #    profit=Count('id', filter=Q(income__gt=F('expenditure'))),
   #    loss = Count('id', filter=Q(income__lt=F('expenditure'))),
   # )

   # print(sales)

   sale = models.Sale.objects.get(id=1)
   print(type(sale))
   print(sale.income)

   models.Sale.objects.filter(id=1).update(income=60)
   sale.refresh_from_db()
   print(sale.income)
   pprint(connection.queries)
