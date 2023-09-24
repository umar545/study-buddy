from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
rooms = [
    {'id': 1, 'name': 'Let"s build python apps'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Welcome , Front end developer'},
]


def HomeView(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def RoomView(request , id):
    room = {}
    for r in rooms :
        if r['id'] == int(id) :
            room = r
    context = {'room' : room} 
    return render(request, 'room.html', context )
