from django.db import models
from django.contrib.auth.models import User # so that every user will see only their part

# Create your models here.
class ToDoList(models.Model): # create a database object "ToDoList"
    name = models.CharField(max_length=200) # we create as a class variable, the variable and the type of the attribute
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)



    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # we use a foreignkey for when we create an item and use cascade as delete so when we delete the todolist since the items are on a todolist we delete them aswell

    text = models.CharField(max_length=300) # string
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
