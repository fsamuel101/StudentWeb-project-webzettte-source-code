from django.forms import ModelForm
from .models import Room, User, Wall
from django.contrib.auth.forms import UserCreationForm
from django import forms
from ckeditor.widgets import CKEditorWidget

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    student_number = forms.CharField(max_length=8, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'student_number', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class RoomForm(ModelForm):
    class Meta:
        model = Room        #where to we use our form
        fields = '__all__' #automatically create the form
        exclude = ['host', 'participants']
        
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar', 'bio']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Wall
        fields = ['name', 'body']
        widgets = {
            'body': CKEditorWidget(),
            'body': forms.Textarea(attrs={'class': 'input-field'}),
            'name': forms.TextInput(attrs={'class': 'input-field'}),
        }
