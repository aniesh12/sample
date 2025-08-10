from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import logout
# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def user_login(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invaid username or password')


    return render(request,'login.html')



def sign_lo(request):
  if request.method == 'POST':
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')
      conform_password=request.POST.get('conform_password')

      if password != conform_password:
          messages.error(request,'Password do not match')
          return render(request,'sign.html')
      if User.objects.filter(username=username).exists():
          messages.error(request,'User name already taken')
          return render(request,'sign.html')
      
      user=User.objects.create_user(username=username,email=email,password=password)
      login(request,user)
      return redirect('home')
  return render(request,'sign.html')

def ownership(request):
    return render(request,'ownership.html')
def service(request):
    return render(request,'service.html')

def logout_us(request):
    logout(request)
    return redirect('user_login')


