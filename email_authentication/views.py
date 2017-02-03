from django.shortcuts import render, redirect
from django.contrib.auth import login
from email_authentication.email_auth_backend import PasswordlessAuthBackend
from django.http import HttpResponse, HttpResponseRedirect
import settings


def login_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        b = PasswordlessAuthBackend()
        user = b.authenticate(email=email, name=name, password=1)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/appointment/swingtime/', {'user': user})
        else:
            return HttpResponseRedirect('/appointment/login/')

    return render(request, 'email_authentication/login.html')
