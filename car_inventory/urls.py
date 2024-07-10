from django.urls import path
from . import views
urlpatterns = [
    path('car/<int:car_id>/', views.car, name='car_details'),
]
