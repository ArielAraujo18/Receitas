from django.urls import path
from . import views

#Http request <- http response

#HTTP REQUEST

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
