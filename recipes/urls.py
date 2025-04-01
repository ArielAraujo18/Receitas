from django.urls import path
from django.http import HttpResponse
from recipes.views import home

#Http request <- http response

#HTTP REQUEST

urlpatterns = [
    path('home/', home), #Home
    path('', home),
]
