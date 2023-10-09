from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Room , Topic , User , Message
from django.db.models import Q
from .forms import RoomForm

def LoginRegister(request):
    page = 'login'
    if request.user.is_authenticated :
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try :
            user = User.objects.get(
                username=username
                )
        except :
            messages.error(request, "user is not present")
        
        user = authenticate(request , username=username , password = password)
        if user is not None :
            login(request, user)
            return redirect('home')
        else :
            messages.error(request , 'username or password is incorrect')
    context ={'page' : page}

    return render(request , 'login.html' , context)
def SginUpRegister(request):
    page='signup'
    form = UserCreationForm()
    context ={'page':page , 'form' : form }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('Success :::::::::::::::::::::' , request.POST.get('username') , request.POST.get('password1'),request.POST.get('password2'))
        if form.is_valid():
            user = form.save(commit=False)
            user.username =user.username.lower()
            user.save()
            login(request , user)
            return redirect('home')
        else :
           messages.error(request , 'please enter the valid info')
    return render(request, 'login.html', context)

def LogoutRegister(request):
    logout( request)
    return redirect('home')

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
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    print(participants , "pppppppppppppppppp")
    context = {'room' : room , 'room_messages': room_messages , 'participants' : participants} 
    if request.method =='POST' :
        message = Message.objects.create(
            user = request.user,
            room = room ,
            body = request.POST.get('message')
        )
        room.participants.add(request.user)
        message.save()
    return render(request, 'room.html', context )
def CreateRoomView(request) :
    form = RoomForm()
    context = {'form': form}
    form = RoomForm(request.POST)
    if form.is_valid() :
        form.save()
        return redirect('home')
    return render( request, 'room-form.html' , context)

@login_required(login_url='login')
def UpdateRoomView (request , pk ) :
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    if request.user != room.host :
        return redirect('home')
    context = {'form' : form}
    if request.method == 'POST' :
        form = RoomForm(request.POST , instance=room)
        if form.is_valid() :
            form.save()
            return redirect('home')
    return render(request , 'room-form.html' , context)
    
def DeleteRoomView(request , pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    context = {'obj' : room}
    if request.method == 'POST' :
        room.delete()
        return redirect('home')
    return  render(request , 'delete.html' , context)
# def DeleteMessageView(request , pk):
#     message = Message.objects.get(id = pk)
#     # form = RoomForm(instance=room)
#     context = {'obj' : message}
#     if request.method == 'POST' :
#         message.delete()
#         return redirect('room ')
#     return  render(request , 'delete.html' , context)
