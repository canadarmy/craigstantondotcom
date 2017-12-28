from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.general_blog, name="general_blog_home"),
    url(r'^(?P<id>[0-9]+)', views.blog_post, name="specific_post"),
]
