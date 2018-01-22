from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests
import json

from .serializers import CryptocurrenciesSerializer
from .models import Blockchain,BCChoice,Cryptocurrencies


#from . import forms

# Create your views here.

def blockchain(request):
    options = Blockchain.BC_CHOICES
    choices = Blockchain.objects.all()

    context = {
        'options': options,
        'choices': choices
    }

    return render(request, "blockchain.html", context)

class CryptoRequests(APIView):
    """docstring for CryptoDetails."""

    def get(self, request):
        cryptos = Cryptocurrencies.objects.all()
        serializer = CryptocurrenciesSerializer(cryptos, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def cryptoview(request):
    latest_fetch = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    fetch_json = latest_fetch.text
    fetch_status = latest_fetch.json()


    for crypto in fetch_status:
        Cryptocurrencies.objects.create(
        name=crypto.get("name"),
        name_id=crypto.get("id"),
        symbol=crypto.get("symbol"),
        rank=crypto.get("rank"),
        price_usd=crypto.get("price_usd"),
        price_btc=crypto.get("price_btc"),
        volume_24h_usd=crypto.get("24h_volume_usd"),
        market_cap_usd=crypto.get("market_cap_usd"),
        available_supply=crypto.get("available_supply"),
        total_supply=crypto.get("total_supply"),
        max_supply=crypto.get("max_supply"),
        percent_change_1h=crypto.get("percent_change_1h"),
        percent_change_24h=crypto.get("percent_change_24h"),
        percent_change_7d=crypto.get("percent_change_7d"),
        last_updated=crypto.get("last_updated")
        )

    data = Cryptocurrencies.objects.filter(name="Bitcoin")

    context = {
        "fetch_json": fetch_json,
        "fetch_status": fetch_status,
        "data": data
    }

    return render(request, "cryptocurrencies.html", context)
