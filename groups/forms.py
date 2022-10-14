import email
from tkinter.ttk import Widget
from django import forms

from groups.models import Category, Tag ,Group,Teacher,Student

class CreateCourseForm(forms.Form):
    name = forms.CharField(required=True)
    category = forms.ModelChoiceField(queryset = Category.objects.all())
    description = forms.CharField(max_length=200,widget=forms.widgets.Textarea)
    image = forms.ImageField()
    mentor = forms.ModelChoiceField(queryset = Teacher.objects.all())
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget = forms.widgets.CheckboxSelectMultiple)

    def clean_name(self):
        new_name = self.cleaned_data['name']
        if Group.objects.filter(name = new_name ):
            raise forms.ValidationError("Имя курса занято")
        return new_name

    def clean_surname(self):
        new_surname = self.cleaned_data['surname']
        if Student.objects.filter(surname = new_surname):
            raise forms.ValidationError("Фамилия занята")
        return new_surname

    def create_course(self):
        group = Group.objects.create(
            name=self.cleaned_data['name'],
            categories=self.cleaned_data['category'],
            description=self.cleaned_data['description'],
            image=self.cleaned_data['image'],
            mentor = self.cleaned_data['mentor']
        )
        group.tags.add(*self.cleaned_data['tags'])
        return group

class CreateStudentForm(forms.Form):
    name = forms.CharField(required=True, strip=True)
    surname = forms.CharField(required=True, strip=True)
    age = forms.IntegerField(required=True)
    email = forms.CharField(required=True)
    group = forms.ModelChoiceField(queryset = Group.objects.all())

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Вам меньше 18 ! Подрастите ")
        return age

    def create_student(self):
        student = Student.objects.create(
            name = self.cleaned_data['name'],
            surname = self.cleaned_data['surname'],
            age = self.cleaned_data['age'],
            email = self.cleaned_data['email'],
            group = self.cleaned_data['group'],

        )
        return student