from django.urls import path
from .views import RegisterUserView, LoginView, UserProfileView

urlpatterns = [
    path('users/register/', RegisterUserView.as_view(), name='register'),
    path('users/signin/', LoginView.as_view(), name='login'),
    path('users/profile/', UserProfileView.as_view(), name='profile'),
]
