from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def dashboard(request):
    section = 'dashboard'
    return render(request, 'registration/dashboard.html', {'section': section})
