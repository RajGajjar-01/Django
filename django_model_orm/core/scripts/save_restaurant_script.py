from core import models
from django.utils import timezone

def run():
    
    restaurant = models.Restaurant()
    restaurant.name = 'My Italian Restaurant'
    restaurant.date_opened = timezone.now()
    restaurant.longitude = 12.253519
    restaurant.latitude = 42.737683
    restaurant.restaurant_type = models.Restaurant.TypeChoices.ITALIAN

    restaurant.save()

    print("Saved to database.")