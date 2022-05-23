"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from base.views import home
from flight.views import flight, createFlight, flightShow, updateFlight, deleteFlight

urlpatterns = [
    path('', flight, name="flight"),
    path('create-flight/', createFlight, name="create-flight"),
    path('update-flight/<str:pk>/', updateFlight, name="update-flight"),
    path('delete-flight/<str:pk>/', deleteFlight, name="delete-flight"),

    path('<str:pk>/', flightShow, name="flightShow"),

]
