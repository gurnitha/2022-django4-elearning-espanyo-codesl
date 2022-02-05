from django.shortcuts import render,HttpResponse

class UserController():
    
    def register(request):
        return render(request, 'views/user/register.html')