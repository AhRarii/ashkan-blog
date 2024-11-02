from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page for adding a new blog
    path('add_blog', views.add_blog, name='add_blog'),

    # Page for Editing a post
    path('edit_blog/<blog_id>', views.edit_blog, name='edit_blog'),

]
