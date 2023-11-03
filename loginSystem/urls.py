from django.urls import path
from loginSystem import views

urlpatterns = [
    path('', views.index, name="home" ),
]