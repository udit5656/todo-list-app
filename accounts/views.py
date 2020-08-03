from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return HttpResponse("Working")
        else:
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        return render(request, 'registration/login.html')
