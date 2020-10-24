from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from chats.form import ThreadForm
from django.contrib.auth.models import User
from chats.models import Thread,ChatMessage

# Create your views here.

def home(request):
    return render(request,'home.html')


def chats(request):
    if request.user.is_authenticated:
        
        user_threads1 = Thread.objects.filter(first=request.user)
        user_threads2 = Thread.objects.filter(second=request.user)
        connected_list = [] 
        for user in user_threads1:
            connected_list.append(user.second)
        for user in user_threads2:
            connected_list.append(user.first)    

        my_dict= {
            
            'connected':connected_list
        }
        return render(request,'chats.html',my_dict)
    else:
        messages.success(request,"you are not logged in!")
        return redirect('login')    

def aboutus(request):
    return render(request,'about-us.html')


def threadview(request,username):
    
    if request.user.is_authenticated:
        
        thread_obj,created = Thread.objects.get_or_new(request.user,username)
        print(thread_obj)
        all_messages = ChatMessage.objects.filter(thread=thread_obj)
        
        form = ThreadForm()
        return render(request,'thread.html',{'form':form,'username':username,'all_messages':all_messages})
    else:
        messages.success(request,"you are not logged in!")
        return redirect('login')  