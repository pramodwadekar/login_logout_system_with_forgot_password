from django.db import models
from django.contrib import admin 

class User (models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.Firstname

class student(models.Model):   
    Fullname = models.CharField(max_length=50)
    DOB = models.DateField()
    Email = models.EmailField(max_length=50)
    Age = models.BigIntegerField()
    Gender = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Qualification =models.CharField(max_length=50)
    Subject = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Fullname
    
    # change DataBase Name
    class Meta: 
        # Add Table Name
        db_table = ''
        # Add verbose name 
        verbose_name = 'Student Management System'
        verbose_name_plural = "Student Management System'"







    
