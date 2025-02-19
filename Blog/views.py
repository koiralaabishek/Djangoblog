from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegistrationForm
from content.models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def index(request):
    post=Post.objects.filter(status=True)
    featured_posts=Post.objects.filter(is_featured=True).order_by('updated_at')
    print(featured_posts)
    context={
        'posts':post,
        'featured_posts':featured_posts
        }
    return render(request,'html/content/index.html',context)


def post_detail(request,slug):
    detailpost= get_object_or_404(Post,slug=slug,status=True)
    context={
        'detailposts':detailpost
    }
  
    return render(request,'html/content/post_detail.html',context)


def register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
         form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,'html/content/register.html',context)


# login function
def login(request):
    if request.method =='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect ('dashboard')

    form =AuthenticationForm()
    context={
        'form':form
    }

    return render(request,'html/content/login.html',context)



def logout(request):
    auth.logout(request)
    return redirect('home')