from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blockchain, name="blockchain_home"),
]
