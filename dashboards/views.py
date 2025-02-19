from django.shortcuts import get_object_or_404, redirect, render

from content.models import Category, Post
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm


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
    return render(request,'html/dashboard/post.html')


def logout(request):
    return render(request,'html/dashboard/logout.html')