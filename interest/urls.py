from django.urls import path
from .views import compound_interest_calculator

urlpatterns = [
    path('interest',compound_interest_calculator),
]
