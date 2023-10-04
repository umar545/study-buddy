from django.shortcuts import render, redirect
from .models import Room , Topic
from django.db.models import Q
from .forms import RoomForm

def LoginRegister(request):
    context ={}
    return render(request , 'login.html' , context)

def HomeView(request):
    q= request.GET.get('q') if request.GET.get('q') != None else '' 
    rooms = Room.objects.filter( 
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q) |
        Q(host__username__icontains = q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms , 'topics' : topics , 'room_count' : room_count}
    return render(request, 'home.html', context)


def RoomView(request , pk):
    room = Room.objects.get(id = pk)
    context = {'room' : room} 
    return render(request, 'room.html', context )

def CreateRoomView(request) :
    form = RoomForm()
    context = {'form': form}
    form = RoomForm(request.POST)
    if form.is_valid() :
        form.save()
        return redirect('home')
    return render( request, 'room-form.html' , context)


def UpdateRoomView (request , pk ) :
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    context = {'form' : form}
    if request.method == 'POST' :
        form = RoomForm(request.POST , instance=room)
        if form.is_valid() :
            form.save()
            return redirect('home')
    return render(request , 'room-form.html' , context)
    # form = RoomForm(request.POST , instance=room) 
    # if form.is_valid() :
    #     form.save()
    #     return redirect('home')

def DeleteRoomView(request , pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    context = {'obj' : room}
    if request.method == 'POST' :
        room.delete()
        return redirect('home')
    return  render(request , 'delete.html' , context)
