from django.shortcuts import render,HttpResponse
from App.Models.User_forms import SignUpForm

class UserController():
    
    def register(request):
        if request.method == "POST":
            pass
        else:
            context = {'form': SignUpForm()}
            return render(request, 'views/user/register.html',context)