from django.shortcuts import render
from core import models
from django.db.models import Sum, Prefetch
from django.utils import timezone

def index(request):
    # restaurants = models.Restaurant.objects.filter(name__istartswith='c').prefetch_related('ratings', 'sales')
    # ratings = models.Rating.objects.select_related('restaurant')
    # ratings = models.Rating.objects.only('rating', 'restaurant__name').select_related('restaurant')

    # Get all 5-star ratings, and fetch all the sales for restaurants with 5-start ratings
    # restaurants = models.Restaurant.objects.prefetch_related('ratings', 'sales').filter(ratings__rating=5).annotate(total = Sum('sales__income'))
    # print(restaurants)

    # Get all 5-star ratings, and fetch all the sales for restaurants with 5-start ratings and sum of tthe sales of last month
    # month_ago = timezone.now() - timezone.timedelta(days=30)
    # print(month_ago)
    # monthly_sales = Prefetch(
    #     'sales',
    #     queryset = models.Sale.objects.filter(datetime__gte = month_ago)
    # )
    # restaurants = models.Restaurant.objects.prefetch_related('ratings', monthly_sales).filter(ratings__rating=5).annotate(total = Sum('sales__income'))

    # print([r.total for r in restaurants])

    jobs = models.StaffRestaurant.objects.prefetch_related('restaurant', 'staff')

    for job in jobs:
        print(job.restaurant.name)
        print(job.staff.name)
        print()

    return render(request, 'core/index.html') 
