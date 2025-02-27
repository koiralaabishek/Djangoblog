from django import forms

from content.models import Category, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','category','featured_image','short_description','blog_body','status')