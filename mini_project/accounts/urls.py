from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register', views.UserCreate.as_view(), name='account-create'),
    path('login', obtain_auth_token, name='login'),
]
