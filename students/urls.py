from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Import here
from .views import register, logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),  # Corrected import
    path('logout/', logout, name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Optional: For token refresh
]
