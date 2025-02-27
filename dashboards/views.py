from django.shortcuts import get_object_or_404, redirect, render

from content.models import Category, Post
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm, PostForm
from django.template.defaultfilters import slugify

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    categpry_count=Category.objects.all().count()
    post_count=Post.objects.all().count()
    context={
        'category_count':categpry_count,
        'post_count':post_count
    }
    
    return render(request,'html/dashboard/dashboard.html',context)




def category(request):
    return render(request,'html/dashboard/category.html')



def add_category(request):
    
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    form=CategoryForm()
    context={
        'form':form
    }
    return render(request,'html/dashboard/add_category.html',context)


def edit_category(request,pk):
    
  
    
    category=get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance =category )
        if form.is_valid():
            form.save()
            return redirect('category')
    form=CategoryForm(instance=category)
    context={
        'form':form
    }
    
    return render(request,'html/dashboard/edit_category.html',context)


def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('category')


def post(request):
    blog=Post.objects.all()
    context={
        'blogs':blog
    }    
    return render(request,'html/dashboard/post.html',context)


def add_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False) # commit=False means that the form data is not yet saved to the database
            post.author=request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title) +'-'+str(post.id)   
            post.save()        
            return redirect('post')
        else:
            print(form.errors)
    
    form=PostForm()
    context={
        'form':form
    }
    return render(request,'html/dashboard/add_post.html',context)


def edit_post(request,pk):
     post=get_object_or_404(Post,pk=pk)
     if request.method=='POST':
         form=PostForm(request.POST,request.FILES,instance=post)
         if form.is_valid():
             post=form.save()
             title=form.cleaned_data['title']
             post.slug=slugify(title) +'-'+str(post.id)
             post.save()
             return redirect('post')
     form=PostForm(instance=post)    
     context={
            'form':form,
            'post':post
     }
     return render(request,'html/dashboard/edit_post.html',context)


def delete_post(request,pk):
    
    post= get_object_or_404(Post,pk=pk)
    post.delete()
    
    return redirect('post')


def logout(request):
    return render(request,'html/dashboard/logout.html')