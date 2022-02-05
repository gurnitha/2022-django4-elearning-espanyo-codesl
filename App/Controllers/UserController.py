from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from App.Models.User_forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import auth

class UserController():
    
    def register(request):
        dataEmail = None
        template = 'views/user/register.html'
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                userdb = User.objects.filter(email=email)
                for item in userdb:
                    dataEmail = item.email
                if dataEmail != None:
                    context = {'form': form,'error':'El email ya existe.'}
                    return render(request,template ,context)
                else:
                    password = form.cleaned_data.get('password')
                    username = form.cleaned_data.get('user')
                    first_name = form.cleaned_data.get('first_name')
                    last_name = form.cleaned_data.get('last_name')
                    User.objects.create_user(username=username,
                                               first_name=first_name,
                                               last_name=last_name,
                                               email=email,
                                               password=password,
                                               is_staff=1)
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request, user) 
                    return HttpResponseRedirect("admin/")
            else:
                context = {'form': form}
                return render(request, template,context)
        else:
            context = {'form': SignUpForm()}
            return render(request, template,context)