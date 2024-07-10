from django.urls import path
from .views import CustomLoginView, SignUpView
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.user_profile, name='profile'),
    path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
