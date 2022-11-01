from django.urls import path
from . import views

urlpatterns=[
    path('seller_home',views.home)
]
