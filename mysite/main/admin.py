from django.contrib import admin
from .models import ToDoList,Item

# Register your models here.

admin.site.register(ToDoList) # to see the ToDoLists 
admin.site.register(Item)