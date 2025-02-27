from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('category/',views.category,name='category'),
    path('category/add',views.add_category,name='add_category'),
    path('category/edit/<int:pk>/',views.edit_category, name="edit_category"),
    path('category/delete/<int:pk>/',views.delete_category, name="delete_category"),
    
    # blog post crud
    
    
    path('post/',views.post,name='post'),
    path('post/add/',views.add_post, name="add_post"),
    path('post/edit/<int:pk>/',views.edit_post, name="edit_post"),
    path('post/delete/<int:pk>/',views.delete_post, name="delete_post"),
    
    
    
    
    path('logout/',views.logout,name='logout'),
    
]
