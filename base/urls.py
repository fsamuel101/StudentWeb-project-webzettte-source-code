#the urls for specific appp

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('admissions/', views.admissions, name = "admissions"),
    path('announcement/', views.announcement, name = "announcement"),
    path('about/', views.about, name = "about"),
    path('faculty/', views.faculty, name = "faculty"),
    path('achievements/', views.achievements, name = "achievements"),
    path('shop/', views.shop, name = "shop"),
    path('developers/', views.developers, name = "developers"),
    path('message-us/', views.message, name = "message-us"),
    path('endUser/', views.endUser, name = "endUser"),
    path('wall/', views.wall, name = "wall"),
    path('create-post/', views.create_post, name = "create-post"),
    path('terms/', views.terms, name = "terms"),
    path('profile/<str:pk>', views.userProfile, name = "user-profile"),
    
    
    
    path('login/', views.loginPage, name = "login"),
    path('register/', views.registerPage, name = "register"),
    path('logout/', views.logoutUser, name = "logout"),
    path('forum/', views.forum, name = "forum" ),
    path('room/<str:pk>/', views.room, name = "room"), #primary key =>>pk passing in the id in the url
    path('create-room', views.createRoom, name = "create-room"),
    path('update-room/<str:pk>', views.updateRoom, name = "update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name = "delete-room"),
    path('update-user/', views.updateUser, name = "update-user"),
    
]



