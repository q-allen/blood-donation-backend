from django.urls import path
from .views import hospitalList

urlpatterns = [
    path('hospitals/', hospitalList.as_view(), name='hospital-list'),
    
]

