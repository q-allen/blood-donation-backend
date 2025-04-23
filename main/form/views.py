from rest_framework import generics
from .models import BloodDonation
from rest_framework import generics, status
from .serializers import BloodDonationSerializer
from rest_framework.response import Response
import logging


class BloodDonationCreateView(generics.CreateAPIView):
    queryset = BloodDonation.objects.all()
    serializer_class = BloodDonationSerializer

  