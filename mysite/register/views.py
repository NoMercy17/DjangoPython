from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            form.save() # save the user in the users database
        return redirect("/") # after we saved the user we go to the home page
    else:
        form = RegisterForm()
   
    form = RegisterForm()
    return render(response, "register/register.html",{"form": form})
    # we pass at the /register the register.html(kinda)