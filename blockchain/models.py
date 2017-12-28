from django.db import models

# Create your models here.

class Blockchain(models.Model):
    BC_CHOICES = (
        ('COIN', 'Buy Coins'),
        ('CONTRACT', 'Contract Craig'),
        ('TEST', 'Test Blockchain'),
    )
    name = models.CharField(max_length=60)
    selection = models.CharField(max_length=1, choices=BC_CHOICES)

    def __str__(self):
        return self.name

class BCChoice(models.Model):
    choice = models.ForeignKey(Blockchain, on_delete=models.CASCADE)
