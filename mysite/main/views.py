from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoList
from .forms import CreateNewList
# Create your views here

def index(response, id):
        ls = ToDoList.objects.get(id = id)

        # implementation so we don t access another todolist that is not ours
        if ls in response.user.todolist.all():

                # {"save":[], "c1":["clicked"]}   {"save":[value="save"]}
                if response.method == "POST":
                        print(response.POST)
                        if response.POST.get("save"):  # if save isn t there we just don't run the block, return None
                                for item in ls.item_set.all():
                                        if response.POST.get("c" + str(item.id)) == "clicked":
                                                item.complete=True
                                        else:
                                                item.complete=False

                                        item.save()

                        elif response.POST.get("newItem"):
                                txt = response.POST.get("new")
                                if len(txt) > 2:
                                        ls.item_set.create(text=txt, complete=False)
                                else:
                                        print("Invalid input!")
                                
                return render(response,"main/list.html",{"ls":ls})
        return render(response,"main/view.html",{"ls":ls})

def home(response):
        return render(response,"main/home.html",{})

def create(response):
        if response.method == "POST":
                form = CreateNewList(response.POST) #contain a dict with id for our attributes and saves the values that we type in them 

                if form.is_valid():
                        n = form.cleaned_data["name"]
                        t = ToDoList(name = n)
                        t.save()
                        response.user.todolist.add(t)
                        # t = ToDoList(name = n)
                        # t.save()

                return HttpResponseRedirect("/%i" %t.id) # we redirec to the page of the todolist that we just created
        else:
                form = CreateNewList()

        return render(response,"main/create.html",{"form":form})

def view(response):
        return render(response, "main/view.html", {})