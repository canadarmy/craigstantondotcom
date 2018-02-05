from rest_framework import serializers
from .models import Cryptocurrencies

class CryptocurrenciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cryptocurrencies
        fields = '__all__'
