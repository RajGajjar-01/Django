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
    # restaurant = models.Restaurant.objects.values('name', 'date_opened').first()
    # restaurant = models.Restaurant.objects.values(rname = Upper('name'))
    # print(restaurant)
    # print(type(restaurant))

    # IT = models.Restaurant.TypeChoices.ITALIAN
    # ratings = models.Rating.objects.filter(restaurant__restaurant_type = IT).values('rating', 'restaurant__name')
    # print(ratings)

    # restaurants = models.Restaurant.objects.values_list('name')
    # print(restaurants)

    # print(models.Restaurant.objects.aggregate(Count('id'))) 
    # above line prints : {'id__count':14}

    # print(models.Restaurant.objects.aggregate(count=Count('id')))
    # above line prints : {'count':14}

    # print(models.Rating.objects.aggregate(avg = Avg('rating')))
    # {'avg': 3.1666666666666665}

    # Average rating of restaurant 'Bombay Bustle'
    # print(models.Rating.objects.filter(restaurant__name='Bombay Bustle').values('rating'))
    # print(models.Rating.objects.filter(restaurant__name='Bombay Bustle').aggregate(avg_rating = Avg('rating')))

    # Maximum income of of all restaurants
    # print(models.Sale.objects.aggregate(max_income=Max('income')))
    # {'max_income': Decimal('99.8300000000000')}

    # Maximum income of 'Bombay Bustle'
    # print(models.Sale.objects.filter(restaurant__name__iexact='Bombay bUstle').values('income'))
    # print(models.Sale.objects.filter(restaurant__name='Bombay Bustle').aggregate(max_income = Max('income')))
    # {'max_income': Decimal('89.3300000000000')}

    # Minimum income of 'Bombay Bustle'
    # print(models.Sale.objects.filter(restaurant__name='Bombay Bustle').values('income'))
    # print(models.Sale.objects.filter(restaurant__name='Bombay Bustle').aggregate(min_income=Min('income')))
    # {'min_income': Decimal('7')}

    # print(models.Sale.objects.filter(restaurant__name='Bombay Bustle').aggregate(
    #     min=Min('income'),
    #     max=Max('income'),
    #     avg=Avg('income'),
    #     sum=Sum('income'),
    # )) 
    # {'min': Decimal('7'), 'max': Decimal('89.3300000000000'), 'avg': Decimal('40.4488888888889'), 'sum': Decimal('364.040000000000')}

    # To get min, max, sum, avg, stddev, variance of all sales of past month
    # one_month_ago = timezone.now() - timezone.timedelta(days=30)
    # sales = models.Sale.objects.filter(datetime__gte=one_month_ago)

    # pprint(sales.aggregate(
    #     min=Min('income'),
    #     max=Max('income'),
    #     sum=Sum('income'),
    #     avg=Avg('income'),
    #     std_deviation=StdDev('income'),
    #     variance=Variance('income'),
    # ))
    # {'avg': Decimal('51.5964406779661'),
    # 'max': Decimal('95.1100000000000'),
    # 'min': Decimal('5.83000000000000'),
    # 'std_deviation': Decimal('28.2598272550235'),
    # 'sum': Decimal('3044.19000000000'),
    # 'variance': Decimal('798.617836483769')}

    # Fetch all restaurants, and let's assume we want
    # to get the number of characters in the name of the restaurant for eg. 'xyz' == 3
    # restaurant = models.Restaurant.objects.annotate(len_name=Length('name'))
    # print(restaurant.values('name', 'len_name'))

    # Get all restaurants with it's name length greater than 10
    # restaurant = models.Restaurant.objects.annotate(len_name=Length('name')).filter(
    #     len_name__gte=13
    # )

    # print(restaurant)
    # <QuerySet [<Restaurant: Bombay Bustle-4>, <Restaurant: Golden Dragon-3>]>

    # To get such an output: Restaurant 1 [Rating: 4.3] --> Rating is average rating 
    concatination = Concat(
        'name', Value(' Rating ['), Avg('ratings__rating'), Value(']'),
        output_field=CharField()
    )

    # restaurants = models.Restaurant.objects.annotate(message=concatination).order_by('name')
    
    # for r in restaurants:
    #     print(r.message)

    # Bombay Bustle Rating [4.0]
    # Chinese 2 Rating [3.0]
    # Chinese 3 Rating [4.0]
    # Golden Dragon Rating [3.25]
    # Indian 2 Rating []
    # Italian 1 Rating [3.0]
    # McDonalds Rating [3.75]
    # Mexican 1 Rating []
    # Mexican 2 Rating [2.0]
    # Pizzeria 1 Rating [1.33333333333333]
    # Pizzeria 2 Rating [3.0]
    # Pizzeria 3 Rating [3.33333333333333]
    # Pizzeria 4 Rating []
    # Taco Bell Rating []


    # To get total sale for all restaurants as --> Restaurant name -- Sales: 123

    # concatination = Concat(
    #     'name', Value(' -- Sales: '), Sum('sales__income'),
    #     output_field=CharField()
    # )

    # restaurants = models.Restaurant.objects.annotate(message = concatination)

    # for r in restaurants:
    #     print(r.message)

    # Pizzeria 1 -- Sales: 409.63
    # Pizzeria 2 -- Sales: 470.04
    # Golden Dragon -- Sales: 323.01
    # Bombay Bustle -- Sales: 364.04
    # McDonalds -- Sales: 255.72
    # Taco Bell -- Sales: 382.27
    # Chinese 2 -- Sales: 477.62
    # Chinese 3 -- Sales: 317.88
    # Indian 2 -- Sales: 178.73
    # Mexican 1 -- Sales: 380.31
    # Mexican 2 -- Sales: 575.18
    # Pizzeria 3 -- Sales: 327.15
    # Pizzeria 4 -- Sales: 525.99
    # Italian 1 -- Sales: 381.0


    pprint(connection.queries)

