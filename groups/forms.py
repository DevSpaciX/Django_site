import email
from itertools import product
from tkinter.ttk import Widget
from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.models import User

from groups.models import Category, Tag ,Group,Teacher,Student

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        self.user = User.objects.filter(username=self.cleaned_data['username']).first()
        if self.user and self.user.check_password(self.cleaned_data['password']):
            return self.cleaned_data
        else:
            raise forms.ValidationError('Username or password is wrong!')
