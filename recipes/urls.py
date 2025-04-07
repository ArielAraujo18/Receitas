from django.urls import path
from . import views

#Http request <- http response

#HTTP REQUEST

urlpatterns = [
    path('', views.home),
    path('recipes/<id>/', views.recipe),
]
