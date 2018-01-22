from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.blockchain, name="blockchain_home"),
    url(r'^cryptocurrencies$', views.cryptoview, name="cryptos_home"),
    url(r'^cryptoapi$', views.CryptoRequests.as_view(), name="cryptos_requests"),

]
