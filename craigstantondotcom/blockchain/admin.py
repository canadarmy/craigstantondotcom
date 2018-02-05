from django.contrib import admin

# Register your models here.
from .models import Cryptocurrencies

class AdminCryptocurrencies(admin.ModelAdmin):
    model = Cryptocurrencies
    list_display = ("symbol","name", "rank")
    list_filter = ["symbol", "name"]
    search_fields = ["symbol", "name"]

admin.site.register(Cryptocurrencies, AdminCryptocurrencies)
