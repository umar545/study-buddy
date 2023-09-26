from django.urls import path
from . import views

urlpatterns = [
    path('' , views.HomeView , name='home'),
    path('room/<str:pk>/', views.RoomView , name='room'),
    path('creat-room/', views.CreateRoomView , name='create-room')
]
