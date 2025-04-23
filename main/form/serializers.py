from rest_framework import serializers
from .models import BloodDonation
from hospitals.models import Hospital

class BloodDonationSerializer(serializers.ModelSerializer):
    hospital = serializers.PrimaryKeyRelatedField(queryset=Hospital.objects.all())
    class Meta:
        model = BloodDonation
        fields = '__all__'
