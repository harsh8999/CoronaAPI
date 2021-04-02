from .views import RegisterAPI
from rest_framework.authtoken import views
from django.urls import path
from django.conf.urls import url
from .views import CustomObtainAuthToken, DocumentRegistrationAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/api-token-auth/login/', views.obtain_auth_token),
    path('api/authenticate/', CustomObtainAuthToken.as_view()),
    # path('api/add-hospital/', HospitalAPI.as_view()),  
    path('api/documentregisteration/', DocumentRegistrationAPI.as_view())
]