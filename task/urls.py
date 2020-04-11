from django.urls import path
from .views import get_prime, get_power

urlpatterns = [
    path('prime/', get_prime),
    path('email/', get_power),
]
