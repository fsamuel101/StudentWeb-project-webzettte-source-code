from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message, Announcement, User, Faculty, Achievement, Council, Items, Developers, Wall

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Announcement)
admin.site.register(User)
admin.site.register(Faculty)
admin.site.register(Achievement)
admin.site.register(Items)
admin.site.register(Developers)
admin.site.register(Wall)