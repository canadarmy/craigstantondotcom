from django.shortcuts import render, get_object_or_404
from bs4 import BeautifulSoup
import mistune

from .models import GeneralBlog
from django.conf import settings
from .templatetags.templatetags import HighlightRenderer


import os


# Create your views here.

def general_blog(request):
    msg = "Blog posts by category:"
    blog_posts = GeneralBlog.objects.all()
    context = {
        "msg": msg,
        "blog_posts": blog_posts
    }
    return render(request, "generalblog.html", context)

def blog_post(request, id):
    specific_post = get_object_or_404(GeneralBlog, pk=id)
    post_name = os.path.basename(str(specific_post.post_content))
    post_location = settings.BASE_DIR + '\\static\\blogfiles\\' + post_name
    post_open = open(post_location, 'r')
    post_read = post_open.readlines
    soup = BeautifulSoup(post_open, "html.parser")
    pretty_soup = soup.prettify()

    #prettier_soup = HighlightRenderer.block_code(pretty_soup, code="```", lang="python")



    context = {
        'specific_post': specific_post,
        'post_read': post_read,
        'pretty_soup': pretty_soup
    }

    return render(request, "blogpage.html", context)
