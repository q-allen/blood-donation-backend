from django.urls import path
from .views import BloodDonationCreateView

urlpatterns = [
    path('blood_donation/', BloodDonationCreateView.as_view(), name='blood-donation-create'),
]
