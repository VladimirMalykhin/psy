from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class UserCreateForm(UserCreationForm):
    # email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class AuthForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "password"]

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ["text"]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["text"]


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        exclude = ["created_at", "user", "is_readed"]


class AnketaForm(forms.ModelForm):
    class Meta:
        model = Answers
        exclude = ["psyhotype", "user"]


class ChangeColorForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bg", "has_music"]


class AddHomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['task']


class SendHomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['answer']


class CheckHomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['comment']
