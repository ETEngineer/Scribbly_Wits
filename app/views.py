from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import models
from .models import Blogs

# Create your views here.
def landing(request):
    if request.method == 'GET':
        return render(request, 'landing.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(uname, email, password)
        user.save()
        return redirect('login')


def home(request):
    if request.method == 'GET':
        content = {
            'blogs' : Blogs.objects.all().order_by('-date')
        }
        return render(request, 'home.html', content)


def post(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        newBlog = models.Blogs(title=title, content=content, author=author)
        newBlog.save()
        return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('landing')

def my_blogs(request):
    content = {
        'blogs' : Blogs.objects.filter(author=request.user)
    }
    return render(request, 'my_blogs.html', content)