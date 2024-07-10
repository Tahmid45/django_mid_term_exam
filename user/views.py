from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from car_inventory.models import Car, CarCategory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
    template_name = 'login.html'  
    def get_success_url(self):
        return reverse_lazy('homepage')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html' 
    success_url = reverse_lazy('login')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserCreationForm(request.POST, instance=request.user)
        profile_form.save()
        return redirect('profile')
    else:
        profile_form = UserCreationForm(instance=request.user)
    return render(request, 'profile.html', {'profile_form': profile_form})


@login_required
def user_profile(request):
    bought_cars = request.user.bought_cars.all()
    return render(request, 'profile.html', {'bought_cars':bought_cars})
@login_required
def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.buyers.add(request.user)
    return redirect('homepage')