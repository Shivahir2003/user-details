from django.urls import path,include
from get_data.views import get_details

urlpatterns = [
    
    path("",get_details),
]