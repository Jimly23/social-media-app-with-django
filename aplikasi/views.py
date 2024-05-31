from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db import IntegrityError
from .forms import *
from django.http import HttpResponseForbidden

# Create your views here.

# DASHBOARD VIEW
@login_required
def dashboard_view(request):
    posts = Posting.objects.all().order_by('-date_post')
    return render(request, 'dashboard.html', {'posts': posts})

# REGISTER VIEW
def register_view(request):
    if request.POST:
        form = Register(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                profile = ProfileUser(user=user)
                profile.save()

                return redirect('dashboard')
        except IntegrityError as e:
            form.add_error('username', 'Nama pengguna sudah ada. Pilih nama pengguna lain.')
    else:
        form = Register()
    return render(request, 'register.html', {'form': form})

# LOGIN VIEW
def login_view(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, f'email or password is wrong!')
            return redirect('login')
    else:
        form = Login()
    return render(request, 'login.html', {'form':form})

# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('login')


# ADD PROFILE IMAGE
def add_image_profile(request, user_id):
    profile = ProfileUser.objects.get(user_id=user_id)
    posting = Posting.objects.filter(user_id=user_id)

    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()

            for post in posting:
                post.profile_pic = f"/media/{profile.image}"
                post.save()

            return redirect('dashboard')
        
    form = ProfileForm()
    return render(request, 'image_profile.html', {'form':form})


# PROFILE VIEW
def profile_view(request, user_id):
    posts = Posting.objects.filter(user_id = user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'profile.html', {'posts': posts,'user':user})

def edit_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    if request.POST:
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = UpdateForm(instance=user)
    return render(request, 'update_profile.html', {'form':form})

# POSTING VIEW
def posting_view(request):
    if request.POST:
        form = PostingForm(request.POST)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.user = request.user
                user = User.objects.filter(email=request.user).first()
                image = user.profileuser.image.url
                post.profile_pic = image
                post.save()
                return redirect('dashboard')
            except:
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('dashboard')
        else:
            messages.warning(request, 'harus di isi')
            return redirect('posting')
    
    form = PostingForm()
    return render(request, 'posting.html', {'form': form})

# DELETE POSTING
def delete_posting_view(request, post_id):
    posting = Posting.objects.get(id=post_id)
    posting.delete()
    return redirect('dashboard')

# BAN USER
def ban_user_view(request, user_id):
    user = User.objects.get(id = user_id)
    user.delete()
    return redirect('dashboard')