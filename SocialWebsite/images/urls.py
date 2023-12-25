from django.urls import path

from .views import imageCreate

app_name="images"

urlpatterns = [
    path('create',imageCreate,name='create')
]
