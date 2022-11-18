from django.urls import path
from app.views import index, get_token, add, multiply, subtract, divide


urlpatterns = [
    path('', index, name="index"),
    path('token/', get_token, name='token'),
    path("add/", add, name="add" ),
    path("multiply/", multiply, name="multiply" ),
    path("subtract/", subtract, name="subtract" ),
    path("divide/", divide, name="divide" ),
]
