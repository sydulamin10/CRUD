from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('Prof/', Prof, name='Prof'),
    path('update/<id>/', update, name='update'),
]
