import email
from urllib import request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method == 'GET':
         return render(request , 'login.html')
    else:
        password = request.POST['password']
        username = request.POST['username']
          
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")    
        else:
           messages.info(request,'invalid credentials')
           return redirect('login')

  
   
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        
       
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
             
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email already in used')
                return redirect('register')
            else:
              user=User.objects.create_user(username = username,password=password1,email = email,first_name = first_name,last_name = last_name)
              user.save();
              messages.info(request,'user taken')
              return redirect('login')
        else:
            messages.info(request,'password is not mathcing')
            return redirect('register')
        
       

    return render(request , 'register.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

