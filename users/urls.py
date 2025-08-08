from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, CustomerProfileView, ArtisanProfileView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('profiles/me/', UserProfileView.as_view(), name='user-profile'),
    path('profiles/customer/', CustomerProfileView.as_view(), name='customer-profile'),
    path('profiles/artisan/', ArtisanProfileView.as_view(), name='artisan-profile'),
]