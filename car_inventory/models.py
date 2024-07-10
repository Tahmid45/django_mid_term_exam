from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CarCategory(models.Model):
    name = models.CharField(max_length=100)
    available_cars = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
        
class Car(models.Model):
    image = models.ImageField(upload_to='static/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE)
    buyers = models.ManyToManyField(User, related_name='bought_cars', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    car = models.ForeignKey(Car, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.car.title}'