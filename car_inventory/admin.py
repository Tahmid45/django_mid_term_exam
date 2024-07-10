from django.contrib import admin
from .models import CarCategory, Car, Comment
# Register your models here.
admin.site.register(Car)
admin.site.register(CarCategory)
admin.site.register(Comment)