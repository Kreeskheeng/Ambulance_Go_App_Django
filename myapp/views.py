from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
############################################################
#from rest_framework.permissions import AllowAny
#from rest_framework.authtoken.models import Token
#from rest_framework.decorators import api_view, permission_classes
#from .models import User


# @api_view(('POST',))
# @permission_classes([AllowAny])
# def api_getToken(request, *args, **kwargs):
 # pass

# @api_view(('POST',))
# #@permission_classes([AllowAny])
# def api_register_view(request, *args, **kwargs):

 #   pass

#######################################################

def home(request):
    return render(request, 'index.html')
  
  

from django.shortcuts import render

def maps(request):
    return render(request, 'maps.html')


# def login_view(request):
  #  if request.method == 'POST':
   #     username = request.POST['username']
    #    password = request.POST['password']
     #   user = authenticate(request, username=username, password=password)
      #  if user is not None:
       #     login(request, user)
        #    return redirect('home')
        #else:
         #   return render(request, 'login.html', {'error': 'Invalid credentials'})
    #else:
     #   return render(request, 'login.html')

# @login_required(login_url='/login/')
# def home_view(request):
  #  return render(request, 'home.html')

# def logout_view(request):
  #  logout(request)
   # return redirect('login')


