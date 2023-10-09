from django.urls import path
from . import views

urlpatterns = [
    path('login' , views.LoginRegister , name='login'),
    path('signup' , views.SginUpRegister , name='signup'),
    path('logout' , views.LogoutRegister , name='logout'),
    path('' , views.HomeView , name='home'),
    path('room/<str:pk>/', views.RoomView , name='room'),
    path('creat-room/', views.CreateRoomView , name='create-room'),
    path('update-room/<int:pk>', views.UpdateRoomView , name='update-room'),
    path('delete-room/<int:pk>', views.DeleteRoomView , name='delete-room')
    # path('delete-message/<int:pk>', views.D , name='delete-room')
]
