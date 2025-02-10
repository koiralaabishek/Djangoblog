from django.shortcuts import render
from django.http import HttpResponse
from content.models import Category,Post
# importing q for or operator
from django.db.models import Q

# Create your views here.

def header(request):

    categories = Category.objects.all()
  
    print(categories)
    context = {
        'categories':categories,
        
    }
    return render(request,'_header.html',context)



def posts_by_category(request,category_id):
    getposts = Post.objects.filter(category=category_id,status='True')
    context = {
    'posts':getposts
}
    
    return render(request,'html/content/post.html',context)


# def recentpost(request):
#     indexposts = Post.objects.filter(status='True')
  
#     context = {
#     'posts':indexposts
# } 
#     return render(request,'html/content/index.html',context)


def search(request):
    keyword = request.GET.get('keywords')
 
    blogs=Post.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status=True)
    
    context={
        'blogs':blogs
    }
    return render(request,'html/content/search.html',context)