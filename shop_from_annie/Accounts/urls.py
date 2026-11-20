from django.urls import path
from .views import Registration, Home



urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register/", Registration.as_view(), name="register"),
]