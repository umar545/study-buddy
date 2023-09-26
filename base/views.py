from django.shortcuts import render
from .models import Room
from .forms import RoomForm
# rooms = [
#     {'id': 1, 'name': 'Let"s build python apps'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Welcome , Front end developer'},
# ]


def HomeView(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def RoomView(request , pk):
    room = Room.objects.get(id = pk)
    context = {'room' : room} 
    return render(request, 'room.html', context )

def CreateRoomView(request) :
    form = RoomForm()
    context = {'form': form}
    return render( request, 'room-form.html' , context)
