from django.shortcuts import render,  get_object_or_404, redirect
from car_inventory.models import Car, CarCategory
# Create your views here.

def home(request, category_id=None):
    categories = CarCategory.objects.all()
    cars = Car.objects.none() 

    if category_id:
        cars = Car.objects.filter(category_id=category_id)
    else:
        cars = Car.objects.all()
    
    if request.user.is_authenticated:
        cars = cars.exclude(buyers=request.user)
    return render(request, 'home.html', {'categories': categories, 'cars': cars})

