from django.urls import path
from .views import results

urlpatterns = [
    path('report/', results, name='report'), 
]
