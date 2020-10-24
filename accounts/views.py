from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.



def signin(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"user created!Now Log-In")
            return redirect('login')
        else:
            messages.success(request,"USER NOT CREATED!Re Sign-In")
            
            return redirect('signin')   
    else:
        form = UserCreationForm()
        return render(request,'signin.html',{'form':form})
