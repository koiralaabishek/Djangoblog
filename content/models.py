from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=5000)
    is_featured = models.BooleanField(default=False)
    status = models.BooleanField(choices=((True,'Published'),(False,'Draft')),default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Posts'