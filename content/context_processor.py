

def categories(request):
    from content.models import Category
    categories = Category.objects.all()
    return {'categories':categories}


# def posts(request):
#     from content.models import Post
#     posts = Post.objects.filter(status=True)
#     return {'posts':posts}

# def posts(request,category_id):
#     from content.models import Post
#     posts = Post.objects.filter(status=True)
#     return {'posts':posts}