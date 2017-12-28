from django.shortcuts import render

from .models import GeneralBlog
from django.conf import settings

import os


# Create your views here.

def general_blog(request):
    msg = "Blog posts by category:"
    blog_posts = GeneralBlog.objects.all()
    return render(request, "generalblog.html", {"msg": msg, "blog_posts": blog_posts})

def blog_post(request, id):
    specific_post = GeneralBlog.objects.get(pk=id)
    post_location = settings.BASE_DIR + str(os.path.abspath(specific_post.post_content))
    post_open = open(post_location, 'rb')
    post_read = print(post_open.read())
    return render(request, "blogpage.html", {'specific_post': specific_post, 'post_read': post_read})
