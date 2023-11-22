from django.urls import path, include
from .views import dashboard, user_register, edit_profile
from django.contrib.auth import views as auth
app_name = 'account'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', user_register, name='register'),
    path('', dashboard, name='dashboard'),
    path('edit/', edit_profile, name='edit_profile')
]
