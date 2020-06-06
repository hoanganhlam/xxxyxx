from django.db import models


class Stock(models.Model):
    isin = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class Histr(models.Model):
    isin = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class sStock(models.Model):
    symbol = models.CharField(max_length=500)
    nct = models.CharField(max_length=500)
    completion_date = models.DateField(auto_now=True)
    phase = models.CharField(max_length=25)
    title = models.CharField(max_length=255)
    conditions = models.CharField(max_length=255)
    interventions = models.CharField(max_length=255)
    market_cap = models.FloatField()
    net_Cash = models.FloatField()
    npv = models.FloatField()
    downside = models.FloatField()
    Upside = models.FloatField()


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
