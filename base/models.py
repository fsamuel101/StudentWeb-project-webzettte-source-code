from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# Create your models here. where we create our database table

#the class that we create represents the table. model of the table in 


#when we added models we need to migrate

class User(AbstractUser):
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField( unique= True, null=True) 
    bio = models.TextField(null=True)
    student_number = models.CharField(max_length=10,null=True)
    
    avatar = models.ImageField(null = True, default="default-dp.jpg", upload_to="user/")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return str(self.username)



class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name





class Room(models.Model):
    host =  models.ForeignKey(User, on_delete = models.SET_NULL, null=True) 
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null=True) #this is the syntax we used to connect two different things
    name = models.TextField(max_length=200, null=True)
    description = RichTextField(blank = True, null=True)
    participants = models.ManyToManyField(User, related_name = 'participants', blank=True)
    updated = models.DateTimeField(auto_now = True)  #when did you update this
    created = models.DateTimeField(auto_now_add=True) #when did we create the room
    
    class Meta:
        ordering = ['-updated', '-created']     #to sort the things out so that the newest is always in the top
    def __str__(self):
        return self.name
    
    
#Every room has a message   
#We have to specify the attruibutes on where we have a message.

class Message(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    body = models.TextField() #leave it alone if you want the user to add some value
    updated = models.DateTimeField(auto_now = True)  #when did you update this
    created = models.DateTimeField(auto_now_add=True) #when did we create the room
    
    def __str__(self):
        return self.body[0:50]  #only 50 character so that we do not have to decluttered our admin panel


class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    description = models.TextField(null = True, blank = True)
    body = RichTextField(blank = True, null=True)
    announcement_image = models.ImageField(null = True, blank=False, upload_to="images/")
    created = models.DateTimeField(auto_now_add=True) #when did we create the room

    
    def __str__(self):
        return self.description
    
    
class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = RichTextField(blank = False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null = True, default="achievements.png", upload_to="achievements/")
    
    def __str__(self):
        return self.title
    
class Faculty(models.Model):
    name = models.TextField()
    position = models.TextField(max_length=200)
    picture = models.ImageField(null = True, default="default-dp.jpg", upload_to="faculty/")
    
    def __str__(self):
        return self.name
    
class Council(models.Model):
    name = models.TextField()
    position = models.TextField(max_length=200)
    picture = models.ImageField(null = True, default="default-dp.jpg", upload_to="council/")
    
    def __str__(self):
        return self.name
    
class Items(models.Model):
    item = models.CharField(max_length=200)
    description = models.TextField(max_length=200);
    price = models.TextField(max_length=20, default='P0.00')
    picture1 = models.ImageField(null=True, blank=True, default="item.jpg", upload_to="shop/")
    picture2 = models.ImageField(null=True, blank=True, default="item.jpg", upload_to="shop/")
    picture3 = models.ImageField(null=True, blank=True, default="item.jpg", upload_to="shop/")
    def __str__(self):
        return self.item
    
    
class Developers(models.Model):
    name = models.TextField()
    role = models.TextField(max_length=200)
    picture = models.ImageField(null = True, default="default-dp.jpg", upload_to="developers/")
    email  = models.EmailField(null = True, blank= False)
    def __str__(self):
        return self.name
    
class Wall(models.Model):
    name = models.CharField(blank=True, max_length=20, default="anonymous")
    body = RichTextField(blank = False, null=True)
    def __str__(self):
        return self.name