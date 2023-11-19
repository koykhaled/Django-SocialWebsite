from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, ProfileForm, EditUserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('account:dashboard')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    section = 'dashboard'
    return render(request, 'registration/dashboard.html', {'section': section})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Update Profile Failed')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = ProfileForm(
            instance=request.user.profile)

    return render(request, 'profile/profile.html', {'user_form': user_form, 'profile_form': profile_form})
