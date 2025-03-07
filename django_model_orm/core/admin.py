from django.contrib import admin
from . import models

# One way to register model on admin panel

# admin.site.register(models.Restaurant)
admin.site.register(models.Sale)
admin.site.register(models.Rating)


# Another way to register model on admin panel

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'website', 'date_opened', 'restaurant_type', 'longitude', 'latitude']

admin.site.register(models.Restaurant, RestaurantAdmin)