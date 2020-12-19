#imports


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .helpers import retrieve_blog_content
# Create your views here.

def home_view(request):
    return HttpResponse("<h1>TODO</h1>")



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data('password1')
            user = authenticate(username=username, password=raw_password)
            #login user
            login(request, user)
            return redirect('blog_view')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #user is logged in
            print('User is logged in!')
            return redirect('blog_view')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form': form })

def blog_view(request):
    if request.method == 'GET':
        blog_content = retrieve_blog_content()
        return render(request, 'myblog.html', {'blog_content': blog_content})
    else:
        return HttpResponse('<h1>TODO</h1>')