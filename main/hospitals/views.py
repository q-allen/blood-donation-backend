from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from .models import Hospital
from .serializers import HospitalSerializer

# Create your views here.
class hospitalList(ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer