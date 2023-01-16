from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Room, Topic, Message, Announcement, User, Faculty, Council, Achievement, Items, Developers, Wall
from .forms import RoomForm, PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from .forms import SignUpForm, UserForm

# Create your views here.


def loginPage(request):
    
    page = 'login'
    
    if request.user.is_authenticated: 
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Username and password does not matched')
            
            
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


APPROVED_STUDENT_NUMBERS = [
    '20-1011',
    '20-1901',
    '20-1111',
    '20-0139',
    '20-0737',
    '20-0290',
    '20-1796',
    '20-0285',
    '20-0018',
    '20-0573',
    '20-2305',
    '20-0124',
    '20-0666',
    '20-0126',
    '19-9023',
    '20-0907',
    '20-2217',
    '20-1819',
    '20-0967',
    '20-2331',
    '20-1011',
    '20-2190',
    '20-1089',
    '20-2197',
    '20-0099',
    '20-2252',
    '19-2347',
    '20-2309',
    '20-0219',
    '19-4343',
    '20-1266',
    '20-1992',
    '20-1345',
    '20-2291',
    '19-2974',
    '20-0225',
    '20-2473',
    '20-2476',
    '20-1483',
    '19-2715',
    '20-0100',
    '20-1667',
    '20-2516',
    '15-292895',
    '20-2312',
    '20-1694',
]



def registerPage(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            student_number = form.cleaned_data['student_number']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            username = form.cleaned_data['username']
            # Check if the student number is in the list of approved student numbers
            if User.objects.filter(student_number=student_number).exists():
                form.add_error('student_number', 'Student Number already in use')
                return render(request, 'base/register.html', {'form': form})
            
            if student_number not in APPROVED_STUDENT_NUMBERS:
                form.add_error('student_number', 'Invalid student number')
                return render(request, 'base/register.html', {'form': form})
            # Check if email is already in use
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already in use')
                return render(request, 'base/register.html', {'form': form})
            # Check if passwords match
            elif password1 != password2:
                form.add_error('password1', 'Passwords do not match')
                return render(request, 'base/register.html', {'form': form})
            # Check if username is already taken
            elif User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken')
                return render(request, 'base/register.html', {'form': form})
                
            else:
                user = form.save(commit=False)      #set to false to actually get the user objects
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, 'An error occured during your registration')
            return render(request, 'base/register.html', {'form': form})
    else:
        return render(request, 'base/register.html', {'form': form})


@login_required(login_url = 'login') 
def forum(request):
    q = request.GET.get('q') if request.GET.get('q') != None  else ''    # q is equal to whatever we pass into the url
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains= q) |
        Q(description__icontains = q)) # it gets the data from database.... We use Q so that we can use or, and , and other stuff here
    user = User.objects.all()
    message = Message.objects.all()
    room_count = rooms.count()
    topics = Topic.objects.all()
    context  = {'rooms': rooms, 'topics': topics, 'room_count': room_count, "user": user, "message": message}
    return render(request, 'base/forum.html', context)

@login_required(login_url = 'login') 
def room(request, pk):  # Pk is primary key
    topics = Topic.objects.all()
    room = Room.objects.get(id = pk )
    room_messages = room.message_set.all().order_by('created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    context = {'room': room, 'room_messages': room_messages, 'participants': participants, 'topics': topics}
    return  render(request, 'base/room.html', context)


def userProfile(request,pk):
    profile = User.objects.all()
    user = User.objects.get(id=pk)
    room = user.room_set.all()
    context = {'user': user, 'room': room, 'profile': profile}
    return render(request, 'base/user-profile.html', context)


@login_required(login_url = 'login')            #the user must log in first
def createRoom(request):
    form  = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)   #get all the data in form 
        if form.is_valid():             #check if the inputs are valid
            room = form.save(commit = False)                 #save the data in the form to the databases
            room.host = request.user
            room.save()
            return redirect('forum')     #redirect the user to the forumpage after adding this
        
    context ={'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url = 'login')  
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)      #get the item that we are going to update
    form = RoomForm(instance=room)      #pass the instance to create a pre filled form
    
    if request.user != room.host:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('forum')
    
    
    context ={'form': form}             #the dictionaru that is going to be in database
    return render(request, 'base/room_form.html',  context)


@login_required(login_url = 'login')  
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        raise PermissionDenied
    
    if request.method == 'POST':
        room.delete()
        return redirect('forum')
    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url = 'login')  
def updateUser(request):
    user = request.user
    form = UserForm(instance = user)
    
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)
    return render(request, 'base/edit-profile.html', {'form' : form})

def admissions(request):
    return render(request, 'base/admissions.html')



def announcement(request):
    announcement = Announcement.objects.all()
    return render(request, 'base/announcement.html', {'announcement': announcement})


def home(request):
    announce = Announcement.objects.all().order_by('-id')[:3]
    context = {'announce': announce}
    return render(request, 'base/home.html',  context)


def about(request):
    return render(request, 'base/about.html')
def shop(request):
    items = Items.objects.all()
    return render(request, 'base/shop.html', {'items': items})

def faculty(request):
    faculty = Faculty.objects.all()
    context = {'faculty': faculty}
    return render(request, 'base/faculty.html', context)

def achievements(request):
    achievement = Achievement.objects.all()
    context = {'achievement': achievement}
    return render(request, 'base/achievements.html', context)

def council(request):
    council = Council.objects.all()
    return render(request, 'base/home.html', {'council': council})

def developers(request):
    developers = Developers.objects.all()
    return render(request, 'base/developers.html', {'developers': developers})

def message(request):
    return render(request, 'base/message-us.html')
def endUser(request):
    return render(request, 'base/EndUser.html') 

def terms(request):
    return render(request, 'base/terms.html')

@login_required(login_url = 'login') 
def wall(request):
    post = Wall.objects.all()
    return render(request, 'base/wall.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wall')
    else:
        form = PostForm()
    return render(request, 'base/create_post.html', {'form': form})



