from django.contrib import admin

# Register your models here.

from .models import Category, Post


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    #list display
    list_display = ('title','category','author','created_at','status','is_featured')
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('status','is_featured')


admin.site.register(Category)
admin.site.register(Post,BlogAdmin)