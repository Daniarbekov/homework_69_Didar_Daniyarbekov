from django.urls import path
from app.views import index, get_token

urlpatterns = [
    path('', index, name="index"),
    path('token/', get_token, name='token'),
]