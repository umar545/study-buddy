from django.urls import path
from . import views

urlpatterns = [
    path('' , views.HomeView , name='home'),
    path('room/<str:id>', views.RoomView , name='room')

]
