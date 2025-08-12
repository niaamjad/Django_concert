from django.urls import path
from .views import LoginView , LogoutView

urlpatterns = [
    path('login/' , LoginView),
    path('logout/' , LogoutView),


]