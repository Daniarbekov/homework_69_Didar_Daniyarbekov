from django.urls import path
from app.views import index, get_token, add

urlpatterns = [
    path('', index, name="index"),
    path('token/', get_token, name='token'),
    path("add/", add, name="add" ),
]