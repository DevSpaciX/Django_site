import email
from enum import unique
from wsgiref.validate import validator
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db import models

def product_upload_path(obj, file):
    return f'product/{obj.id}/{file}'


class Category(models.Model):
    name = models.CharField(max_length = 100, null=True, unique=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length = 100,unique=True)
    image = models.ImageField(upload_to=product_upload_path,null =True)
    description = models.TextField(max_length = 200,null =True)
    tags = models.ManyToManyField("groups.Tag")
    categories = models.ForeignKey(Category,on_delete = models.SET_NULL,null =True)
    mentor = models.ForeignKey("groups.Teacher" , on_delete = models.PROTECT ,null = True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length = 100 , null =True)
    age = models.PositiveIntegerField(default=0 , null =True)
    email = models.EmailField(max_length = 254 , null =True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length = 100 , null =True)
    surname = models.CharField(max_length = 100 , null =True, unique=True) 
    age = models.PositiveIntegerField(default=0 , null =True,validators=[MinValueValidator(18), MaxValueValidator(100)])
    email = models.EmailField(max_length = 254 , null =True, unique=True)
    group = models.ForeignKey(Group, on_delete = models.SET_NULL , null =True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length = 100, null=True , unique=True)

    def __str__(self):
        return self.name

