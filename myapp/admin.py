from django.contrib import admin
from .models import *
from  django.contrib.auth.models  import  Group 

admin.site.register(student)

admin.site.unregister(Group) 

# class  detailsAdmin(admin.ModelAdmin):
#     list_display=('Fullname','DOB','Email','Contact','Gender')

