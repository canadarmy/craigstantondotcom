from django.db import models

# Create your models here.

class Blockchain(models.Model):
    BC_CHOICES = (
        ('COIN', 'Buy Coins'),
        ('CONTRACT', 'Contract Craig'),
        ('TEST', 'Test Blockchain'),
        ('RESEARCH', 'Research')
    )
    name = models.CharField(max_length=60)
    selection = models.CharField(max_length=1, choices=BC_CHOICES)

    def __str__(self):
        return self.name

class BCChoice(models.Model):
    choice = models.ForeignKey(Blockchain, on_delete=models.CASCADE)


class Cryptocurrencies(models.Model):
    """docstring for Cryptocurrencies.
    List of cryptocurrencies and their values
    """
    name = models.CharField(blank=True, max_length=100)
    name_id = models.CharField(blank=True, max_length=100)
    symbol = models.CharField(blank=True, max_length=100)
    rank = models.IntegerField(blank=True, null=True)
    price_usd = models.FloatField(null=True)
    price_btc = models.FloatField(null=True)
    volume_24h_usd = models.FloatField(null=True)
    market_cap_usd = models.FloatField(null=True)
    available_supply = models.FloatField(null=True)
    total_supply = models.FloatField(null=True)
    max_supply = models.FloatField(null=True)
    percent_change_1h = models.FloatField(null=True)
    percent_change_24h = models.FloatField(null=True)
    percent_change_7d = models.FloatField(null=True)
    last_updated = models.IntegerField(blank=True, null=True)


    def __str__(self):
        symbol = self.symbol
        name = self.name
        value = "{}: {}".format(symbol, name)
        return value
