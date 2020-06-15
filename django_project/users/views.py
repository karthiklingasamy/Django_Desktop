from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):

<<<<<<< HEAD
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
  
  else:
    return render(request,'users/register.html',{'form':form})
=======
    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("blog-home")
    else:

        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
>>>>>>> 3b17ad7053926b37b25fa2834f55dff0a680a444
