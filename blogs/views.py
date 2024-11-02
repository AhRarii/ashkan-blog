from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BlogFrom
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """The home page for blogs."""
    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


@login_required
def add_blog(request):
    """Add a blog from a form to the database."""
    if request.method != 'POST':
        form = BlogFrom()
    else:
        form = BlogFrom(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/add_blog.html', context)


@login_required
def edit_blog(request, blog_id):
    """Edit an existing blog."""
    blog = BlogPost.objects.get(id=blog_id)
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogFrom(instance=blog)
    else:
        form = BlogFrom(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)
