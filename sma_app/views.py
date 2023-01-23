from django.shortcuts import redirect,render
from django.contrib.auth import authenticate
from django.contrib import messages 
from sma_app.models import User
# Create your views here.
def home(request):
    return render(request,'index.html')


def sign_up(request):
    
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email is already taken')
                return redirect('signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request,'username is already taken')
                return redirect('signup')
                 
            else:
                 user=User.objects.create_user(username=username,password=password,email=email)
                 user.save()
            
            
        else:
             messages.info(request,'password is not matching')
             return redirect('signup')
             
    
    
    else:
         return render(request,'signup.html')


def signin(request):

    if request.method=="post":
        username=request.post['username']
        password=request.post['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            authenticate.login(request,user)
            return redirect('home')


        else:
            messages.info(request,'user and pasword not exists')  
            return redirect('signup')  


    else:
        return render(request,'signin.html')

