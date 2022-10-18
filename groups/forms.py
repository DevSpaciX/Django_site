import email
from tkinter.ttk import Widget
from django import forms

from groups.models import Category, Tag ,Group,Teacher,Student

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


    def clean_name(self):
        surname = self.cleaned_data['name']
        if Group.objects.filter(name = surname ):
            raise forms.ValidationError("Имя курса занято")
        return surname


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("Вам меньше 18 ! Подрастите ")
        return age

    def clean_surname(self):
        new_surname = self.cleaned_data['surname']
        if Student.objects.filter(surname = new_surname):
            raise forms.ValidationError("Фамилия занята")
        return new_surname