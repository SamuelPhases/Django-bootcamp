from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def allpost(request):
    blog = Blog.objects.all()
    context = {
        'posts': blog
    }
    return render(request, 'blog/allpost.html', context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'post': blog
    }
    return render(request, 'blog/detail.html', context)