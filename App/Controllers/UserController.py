from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from App.Models.User_forms import SignUpForm

class UserController():
    
    def register(request):
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('user')
                return HttpResponse('<h1>Alex Pagoada</h1>%s' % username)
            else:
                context = {'form': form}
                return render(request, 'views/user/register.html',context)
        else:
            context = {'form': SignUpForm()}
            return render(request, 'views/user/register.html',context)