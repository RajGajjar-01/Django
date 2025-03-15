from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GK', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length = 100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)
    capacity = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = [Lower('name')]

    def __str__(self):
        return f'{self.name}-{self.id}'
    
    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)

class Staff(models.Model):
    name = models.CharField(max_length=128)
    restaurants = models.ManyToManyField(Restaurant, through='StaffRestaurant')

    def __str__(self):
        return f'{self.name}'
    
class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    # related_name will change the name of associated manager for backward lookup
    rating = models.PositiveSmallIntegerField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.restaurant}-rating:{self.rating}'

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    expenditure = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.restaurant}-{self.income}-{self.datetime}'
    
